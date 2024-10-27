<script>
    export let open = false;
    export let onSave = () => {};
    export let onClose = () => {};
  
    let title = 'Flood Alert in San Francisco';
    let content = 'Heavy rains have caused flooding in downtown San Francisco. Evacuations are underway.';
    let location = 'San Francisco, CA, USA';
    let image = null;
    let idProof = null;
    let sliderValue = 50; // Bot detection slider default
  
    function handleFileUpload(e, type) {
      const file = e.target.files[0];
      if (type === 'image') image = file;
      if (type === 'id') idProof = file;
    }
  
    function handleSubmit(e) {
      e.preventDefault();
      onSave({
        title,
        content,
        location,
        idProof,
        reportedTime: 'Just Now',
        category: 'Flood',
        postImage: '/banner4.jpg',
        profileImage: '/pfp1.png',
        name: 'Demo User',
      });
      onClose();
    }
  </script>
  
  {#if open}
    <div class="fixed inset-0 z-50 flex items-center justify-center bg-black/50 p-4">
      <div class="bg-white rounded-lg shadow-lg w-full max-w-4xl h-[90%] overflow-y-auto">
        <div class="p-6 grid grid-cols-1 md:grid-cols-2 gap-6">
          <h2 class="col-span-full text-2xl font-bold text-gray-800 mb-2">Add a New Post</h2>
          <p class="col-span-full text-sm text-gray-600">Please provide all required details carefully. Both an image and ID proof are required for verification.</p>
  
          <!-- Title Field -->
          <div class="col-span-full">
            <label class="block text-sm font-medium text-gray-700">Title</label>
            <input
              type="text"
              bind:value={title}
              class="mt-2 w-full p-3 border rounded-md focus:ring-indigo-500 focus:border-indigo-500"
              required
            />
          </div>
  
          <!-- Content Field -->
          <div class="col-span-full">
            <label class="block text-sm font-medium text-gray-700">Content</label>
            <textarea
              bind:value={content}
              rows="4"
              class="mt-2 w-full p-3 border rounded-md focus:ring-indigo-500 focus:border-indigo-500"
              required
            ></textarea>
          </div>
  
          <!-- Location Field -->
          <div class="col-span-full">
            <label class="block text-sm font-medium text-gray-700">Location</label>
            <input
              type="text"
              bind:value={location}
              class="mt-2 w-full p-3 border rounded-md focus:ring-indigo-500 focus:border-indigo-500"
              required
            />
          </div>
  
          <!-- Image Upload -->
          <div class="col-span-1">
            <label class="block text-sm font-medium text-gray-700">Upload Cover Photo</label>
            <div class="mt-2 flex justify-center rounded-lg border border-dashed border-gray-300 px-6 py-10">
              <div class="text-center">
                <input 
                  type="file" 
                  accept="image/*" 
                  on:change={(e) => handleFileUpload(e, 'image')} 
                  class="sr-only"
                />
                <label for="file-upload" class="relative cursor-pointer rounded-md bg-white font-semibold text-indigo-600 hover:text-indigo-500">
                  <span>Upload Photo</span>
                </label>
                <p class="text-xs text-gray-500 mt-2">PNG, JPG, GIF up to 10MB</p>
              </div>
            </div>
          </div>
  
          <!-- ID Upload -->
          <div class="col-span-1">
            <label class="block text-sm font-medium text-gray-700">Upload ID Proof</label>
            <div class="mt-2 flex justify-center rounded-lg border border-dashed border-gray-300 px-6 py-10">
              <div class="text-center">
                <input 
                  type="file" 
                  accept="image/*" 
                  on:change={(e) => handleFileUpload(e, 'id')} 
                  class="sr-only"
                />
                <label for="id-upload" class="relative cursor-pointer rounded-md bg-white font-semibold text-indigo-600 hover:text-indigo-500">
                  <span>Upload ID Proof</span>
                </label>
                <p class="text-xs text-gray-500 mt-2">Upload an image of your ID</p>
              </div>
            </div>
          </div>
  
          <!-- Bot Detection Slider -->
          <div class="col-span-full">
            <label class="block text-sm font-medium text-gray-700">Bot Detection Slider</label>
            <input 
              type="range" 
              min="0" 
              max="100" 
              step="1" 
              bind:value={sliderValue}
              class="mt-2 w-full"
            />
            <p class="text-sm text-gray-500 mt-1">Slide to confirm you're human: {sliderValue}%</p>
          </div>
  
          <!-- Action Buttons -->
          <div class="col-span-full flex justify-end space-x-4 mt-6">
            <button 
              type="button" 
              on:click={onClose} 
              class="px-4 py-2 text-sm text-gray-600 border border-gray-300 rounded-md hover:bg-gray-100"
            >
              Cancel
            </button>
            <button 
              type="submit" 
              on:click={handleSubmit}
              class="px-4 py-2 text-sm font-semibold text-white bg-indigo-600 rounded-md hover:bg-indigo-500"
            >
              Save
            </button>
          </div>
        </div>
      </div>
    </div>
  {/if}
  