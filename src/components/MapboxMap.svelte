<script>
  import { onMount } from 'svelte';
  import mapboxgl from 'mapbox-gl';

  export let accessToken = ''; // Mapbox token
  export let posts = []; // Posts with lat/lng information
  export let onFilterPosts = () => {}; // Callback to notify parent component

  let map; // Reference to the map instance

  // Helper function to calculate the distance between two coordinates (in km)
  function getDistance(lat1, lon1, lat2, lon2) {
    const R = 6371; // Radius of the Earth in km
    const dLat = (lat2 - lat1) * (Math.PI / 180);
    const dLon = (lon2 - lon1) * (Math.PI / 180);
    const a = 
      Math.sin(dLat / 2) ** 2 +
      Math.cos(lat1 * (Math.PI / 180)) *
      Math.cos(lat2 * (Math.PI / 180)) *
      Math.sin(dLon / 2) ** 2;
    const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
    return R * c;
  }

  // Initialize the map and add markers when the component mounts
  onMount(() => {
    mapboxgl.accessToken = accessToken;

    // Create a new Mapbox map
    map = new mapboxgl.Map({
      container: 'map', // Map container element
      style: 'mapbox://styles/mapbox/streets-v11',
      center: [-95.7129, 37.0902], // Default center (USA)
      zoom: 4, // Default zoom level
    });

    // Add markers for each post
    posts.forEach(({ title, lat, lng, content }) => {
      if (lat && lng) {
        const marker = new mapboxgl.Marker() // Simple default marker
          .setLngLat([lng, lat])
          .setPopup(
            new mapboxgl.Popup().setHTML(
              `<strong>${title}</strong><p>${content}</p>`
            )
          )
          .addTo(map);

        // Add click event to filter nearby posts
        marker.getElement().addEventListener('click', () => {
          const nearbyPosts = posts.filter(
            (p) => getDistance(lat, lng, p.lat, p.lng) <= 50 // 50 km threshold
          );
          onFilterPosts(nearbyPosts); // Notify parent component
        });
      }
    });

    // Add zoom and rotation controls to the map
    map.addControl(new mapboxgl.NavigationControl());
  });
</script>

<!-- Map container -->
<div id="map" class="h-full w-full"></div>

<style>
  #map {
    height: 100%;
    width: 100%;
  }
</style>