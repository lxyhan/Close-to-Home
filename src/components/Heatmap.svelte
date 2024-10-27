<script>
  import { onMount } from 'svelte';
  import mapboxgl from 'mapbox-gl';
  import seedrandom from 'seedrandom'; // Import seedrandom library

  const accessToken = 'pk.eyJ1IjoiaGFubHl1MjAwNSIsImEiOiJjbTJxano5dWkxNXo0MmtxODM5MmxwN3lwIn0.2bgd33u52q49s2QcdaMVIg'; // Replace with your token
  let map;

  function generateClusteredPoints(start, radius, numClusters, pointsPerCluster, seed = 'fixed-seed') {
    const rng = seedrandom(seed); // Initialize seeded RNG
    const [lngStart, latStart] = start;
    const clusters = [];

    // Helper function to generate circular clusters
    function generateCircleCluster(clusterCenter, clusterRadius, numPoints) {
      const points = [];

      for (let i = 0; i < numPoints; i++) {
        const angle = rng() * 2 * Math.PI; // Seeded random angle
        const distance = rng() * clusterRadius; // Seeded random distance within radius

        const deltaLat = (distance / 111) * Math.cos(angle); // Convert distance to degrees latitude
        const deltaLng = (distance / (111 * Math.cos(clusterCenter[1] * (Math.PI / 180)))) * Math.sin(angle); // Adjust longitude by latitude factor

        const lat = clusterCenter[1] + deltaLat;
        const lng = clusterCenter[0] + deltaLng;

        const density = Math.floor(rng() * 5) + 1; // Seeded random density
        const name = `Event ${Math.floor(rng() * 100)}`; // Seeded random name

        points.push({
          type: 'Feature',
          geometry: { type: 'Point', coordinates: [lng, lat] },
          properties: { density, name }
        });
      }

      return points;
    }

    // Generate clusters around the starting location
    for (let i = 0; i < numClusters; i++) {
      const clusterAngle = (i / numClusters) * 2 * Math.PI; // Distribute clusters evenly
      const clusterDistance = rng() * radius; // Seeded spread of clusters within the total radius

      const clusterLat = latStart + (clusterDistance / 111) * Math.cos(clusterAngle);
      const clusterLng =
        lngStart + (clusterDistance / (111 * Math.cos(latStart * (Math.PI / 180)))) * Math.sin(clusterAngle);

      const clusterCenter = [clusterLng, clusterLat];
      const clusterRadius = rng() * 2 + 0.5; // Seeded smaller radius for realistic clusters

      const clusterPoints = generateCircleCluster(clusterCenter, clusterRadius, pointsPerCluster);
      clusters.push(...clusterPoints);
    }

    return clusters;
  }

  // Example usage: Generate data centered around New Orleans, LA
  const startPoint = [-90.0715, 29.9511]; // New Orleans coordinates
  const radiusInKm = 8; // Radius for spreading clusters (8 km)
  const numberOfClusters = 6; // Number of clusters
  const pointsPerCluster = 15; // Points per cluster
  const seed = 'hurricane-seed-108'; // Fixed seed for consistent generation

  const data = {
    type: 'FeatureCollection',
    features: generateClusteredPoints(
      startPoint,
      radiusInKm,
      numberOfClusters,
      pointsPerCluster,
      seed
    )
  };

  console.log(data); // Log the generated GeoJSON data

  // Initialize the map
  onMount(() => {
    mapboxgl.accessToken = accessToken;

    map = new mapboxgl.Map({
      container: 'map', // ID of the map container
      style: 'mapbox://styles/mapbox/dark-v10', // Map style
      center: [-90.0715, 29.9511], // Initial center (New Orleans)
      zoom: 11, // Initial zoom level
      bearing: 0 // Optional: Set map rotation to 0
    });

    map.on('load', () => {
      map.addSource('hurricaneImpact', {
        type: 'geojson',
        data: data
      });

      // Add the heatmap layer
      map.addLayer({
        id: 'heatmap-layer',
        type: 'heatmap',
        source: 'hurricaneImpact',
        maxzoom: 15,
        paint: {
          'heatmap-intensity': ['interpolate', ['linear'], ['zoom'], 0, 0.5, 15, 3],
          'heatmap-radius': ['interpolate', ['linear'], ['zoom'], 0, 2, 15, 25],
          'heatmap-color': [
            'interpolate',
            ['linear'],
            ['heatmap-density'],
            0, 'rgba(33, 102, 172, 0)',
            0.2, 'rgb(103, 169, 207)',
            0.4, 'rgb(209, 229, 240)',
            0.6, 'rgb(253, 219, 199)',
            0.8, 'rgb(239, 138, 98)',
            1, 'rgb(178, 24, 43)'
          ],
          'heatmap-opacity': ['interpolate', ['linear'], ['zoom'], 0, 0.5, 10, 1]
        }
      });

      // Add a symbol layer for pins when zoomed out
      map.addLayer({
        id: 'symbol-layer',
        type: 'symbol',
        source: 'hurricaneImpact',
        minzoom: 0,
        maxzoom: 8, // Show pins at lower zoom levels
        layout: {
          'icon-image': 'marker-15',
          'icon-size': 1.2,
          'text-field': ['get', 'name'],
          'text-font': ['Open Sans Semibold', 'Arial Unicode MS Bold'],
          'text-offset': [0, 1.5],
          'text-anchor': 'top'
        },
        paint: {
          'text-color': '#333'
        }
      });
    });

    // Add a popup for each point
    map.on('click', 'heatmap-layer', (e) => {
      const coordinates = e.features[0].geometry.coordinates.slice();
      const { name, density } = e.features[0].properties;

      new mapboxgl.Popup()
        .setLngLat(coordinates)
        .setHTML(`<strong>${name}</strong><p>Impact Density: ${density}</p>`)
        .addTo(map);
    });

    // Add a navigation control
    map.addControl(new mapboxgl.NavigationControl());
  });

  // Cleanup on component destroy
  function cleanup() {
    if (map) map.remove();
  }
</script>

<!-- Map Container -->
<div id="map" class="h-screen w-full"></div>

<style>
  #map {
    height: 100%;
    width: 100%;
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  }
</style>
