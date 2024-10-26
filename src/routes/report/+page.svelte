<script>
    let location = '';
    let type = '';
  
    function submitReport() {
      alert(`Reported ${type} at ${location}`);
    }
  </script>
  
  <h2 class="text-3xl font-bold mt-10">Report a Disaster</h2>
  <form class="mt-4" on:submit|preventDefault={submitReport}>
    <input
      type="text"
      placeholder="Location"
      bind:value={location}
      class="border p-2 mb-2"
    />
    <select bind:value={type} class="border p-2 mb-2">
      <option value="Earthquake">Earthquake</option>
      <option value="Flood">Flood</option>
      <option value="Wildfire">Wildfire</option>
    </select>
    <button type="submit" class="bg-blue-500 text-white p-2">Submit</button>
  </form>
  