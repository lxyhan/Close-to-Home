<script>
  import { onMount } from 'svelte';
  import mapboxgl from 'mapbox-gl';

  export let accessToken = ''; // Mapbox token
  export let posts = []; // List of posts with lat/lng information
  export let onFilterPosts = () => {}; // Callback to notify parent component

  let map; // Map instance reference

  onMount(() => {
    mapboxgl.accessToken = accessToken;

    // Initialize the Mapbox map
    map = new mapboxgl.Map({
      container: 'map',
      style: 'mapbox://styles/mapbox/outdoors-v12',
      center: [0, 0],
      zoom: 1.5,
      pitch: 50,
      bearing: 0,
      projection: 'globe',
    });

    map.on('style.load', () => {
      // Add terrain source
      map.addSource('mapbox-dem', {
        type: 'raster-dem',
        url: 'mapbox://mapbox.terrain-rgb',
        tileSize: 512,
        maxzoom: 14,
      });

      // Add posts as a geojson source with clustering
      map.addSource('posts', {
        type: 'geojson',
        data: {
          type: 'FeatureCollection',
          features: posts.map(({ title, lat, lng, content }) => ({
            type: 'Feature',
            geometry: { type: 'Point', coordinates: [lng, lat] },
            properties: { title, content },
          })),
        },
        cluster: true,
        clusterMaxZoom: 14,
        clusterRadius: 60,
      });

      // Add clustered circles layer
      map.addLayer({
        id: 'clusters',
        type: 'circle',
        source: 'posts',
        filter: ['has', 'point_count'],
        paint: {
          'circle-color': [
            'step',
            ['get', 'point_count'],
            '#FDD835', 10,
            '#FFA726', 30,
            '#EF5350', 50,
          ],
          'circle-radius': [
            'step',
            ['get', 'point_count'],
            20, 10,
            30, 30,
            40, 50,
          ],
          'circle-stroke-width': 2,
          'circle-stroke-color': '#fff',
        },
      });

      // Add cluster count labels
      map.addLayer({
        id: 'cluster-count',
        type: 'symbol',
        source: 'posts',
        filter: ['has', 'point_count'],
        layout: {
          'text-field': '{point_count_abbreviated}',
          'text-font': ['DIN Offc Pro Medium', 'Arial Unicode MS Bold'],
          'text-size': 14,
        },
        paint: { 'text-color': '#fff' },
      });

      // Add individual post markers
      posts.forEach(({ lat, lng, title, content }) => {
        if (lat && lng) {
          const el = document.createElement('div');
          el.className = 'custom-marker';
          el.style.backgroundImage = 'url("/marker-icon.png")';
          el.style.width = '40px';
          el.style.height = '40px';
          el.style.backgroundSize = 'cover';
          el.style.borderRadius = '50%';
          el.style.boxShadow = '0 0 8px rgba(0, 0, 0, 0.4)';

          const marker = new mapboxgl.Marker(el)
            .setLngLat([lng, lat])
            .setPopup(
              new mapboxgl.Popup({ offset: 25 }).setHTML(
                `<strong>${title}</strong><p>${content}</p>`
              )
            )
            .addTo(map);

          // Add click event to filter posts on marker click
          el.addEventListener('click', () => {
            filterPostsByLocation(title);
          });
        }
      });

      // Handle cluster click to zoom in
      map.on('click', 'clusters', (e) => {
        const features = map.queryRenderedFeatures(e.point, { layers: ['clusters'] });
        const clusterId = features[0].properties.cluster_id;

        map.getSource('posts').getClusterExpansionZoom(clusterId, (err, zoom) => {
          if (err) return;
          map.easeTo({ center: features[0].geometry.coordinates, zoom });
        });
      });

      // Add map controls
      map.addControl(new mapboxgl.NavigationControl());
    });
  });

  // Filter posts based on the clicked marker's location or title
  function filterPostsByLocation(title) {
    const filtered = posts.filter((post) => post.title === title);
    onFilterPosts(filtered); // Notify parent component of filtered posts
  }
</script>

<!-- Map container -->
<div id="map" class="h-full w-full"></div>

<style>
  #map {
    height: 100%;
    width: 100%;
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  }

  .custom-marker {
    cursor: pointer;
    transition: transform 0.2s;
  }

  .custom-marker:hover {
    transform: scale(1.2);
  }
</style>
