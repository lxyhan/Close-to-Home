<script>
    export let post = {}; // Post passed in as a prop
  
    // Format date if needed
    function formatDate(timestamp) {
      const date = new Date(timestamp);
      return date.toLocaleString();
    }
  </script>
  
  <div class="p-6 bg-white shadow-md rounded-lg">
    <!-- Post Header -->
    <div class="flex items-center gap-4">
      <img
        class="h-16 w-16 rounded-full object-cover"
        src={post.profileImage}
        alt={post.name}
      />
      <div>
        <p class="text-lg font-semibold text-gray-900">{post.name}</p>
        <p class="text-sm text-gray-500">{post.email}</p>
        <p class="text-xs text-gray-400">
          Posted on {formatDate(post.timestamp)}
        </p>
      </div>
    </div>
  
    <!-- Main Post Content -->
    <div class="mt-4">
      <h2 class="text-2xl font-bold text-gray-900">{post.title}</h2>
      <p class="mt-2 text-gray-700">{post.content}</p>
    </div>
  
    <!-- Post Image -->
    <div class="mt-4">
      <img
        class="w-full h-64 object-cover rounded-lg"
        src={post.postImage}
        alt={post.title}
      />
    </div>
  
    <!-- Location Details -->
    <div class="mt-6">
      <p class="text-sm font-medium text-gray-800">Location:</p>
      <p class="text-sm text-gray-600">
        Latitude: {post.lat}, Longitude: {post.lng}
      </p>
    </div>
  
    <!-- Footer -->
    <div class="mt-6 flex items-center justify-end gap-4">
      <a
        href={`/dashboard`}
        class="px-4 py-2 rounded-md text-sm font-medium text-white bg-indigo-600 hover:bg-indigo-500"
      >
        Back to Dashboard
      </a>
      <button
        class="px-4 py-2 rounded-md text-sm font-medium text-indigo-600 border border-indigo-600 hover:bg-indigo-100"
        on:click={() => window.history.back()}
      >
        Go Back
      </button>
    </div>
  </div>
  
  <style>
    /* Optional: Custom styling for responsiveness */
    @media (min-width: 640px) {
      .post-header {
        flex-direction: row;
      }
    }
  </style>
  