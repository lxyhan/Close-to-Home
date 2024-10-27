<script>
  export let data;
  let { post } = data; // Destructuring the post from data

  console.log('Received post:', post); // Verify the post data

  function goBackToDashboard() {
    window.location.href = '/dashboard'; // Navigate to dashboard or home route
  }

  function handleDonate() {
    alert(`Thank you for considering a donation for ${post.title}. Redirecting...`);
    // Example redirection to a donation page
    window.location.href = `https://buy.stripe.com/test_7sI8z4fig2oN3Pa6oo`;
  }
</script>

<div class="bg-white">
  <!-- Top Buttons: Return and Donate -->

  <div class="mx-auto px-4 py-16 sm:px-6 sm:py-24 lg:max-w-7xl lg:px-8">
    <div class="lg:grid lg:grid-cols-7 lg:grid-rows-1 lg:gap-x-8 lg:gap-y-10 xl:gap-x-16">
      <!-- Post Image -->
      <div class="lg:col-span-4 lg:row-end-1">
        <div class="aspect-h-3 aspect-w-4 overflow-hidden rounded-lg bg-gray-100">
          <img 
            src={post.postImage} 
            alt={`Image of ${post.title}`} 
            class="object-cover object-center" 
          />
        </div>
      </div>

      <!-- Post Details -->
      <div class="mx-auto mt-14 max-w-2xl sm:mt-16 lg:col-span-3 lg:row-span-2 lg:row-end-2 lg:mt-0 lg:max-w-none">
        <div class="mt-4 flex justify-start space-x-4">
          <button 
            on:click={goBackToDashboard} 
            class="relative inline-flex items-center rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 ring-1 ring-inset ring-gray-900 hover:bg-gray-100 focus:z-10"
          >
            Return to Dashboard
          </button>
      
          <button 
            on:click={handleDonate} 
            class="relative inline-flex items-center rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 ring-1 ring-inset ring-gray-900 hover:bg-gray-100 focus:z-10"
          >
            Donate with Stripe
          </button>
        </div>
      
        <div class="flex flex-col-reverse">
          
          <div class="mt-4">
            <h1 class="text-2xl font-bold tracking-tight text-gray-900 sm:text-3xl">
              {post.title}
            </h1>
            <p class="mt-2 text-sm text-gray-500">
              By {post.name} • {post.location} • {new Date(post.reportedTime).toLocaleString()}
            </p>
            <p class="text-sm font-medium text-red-600 mt-2">
              Status: {post.status}
            </p>
          </div>

          <div class="mt-6 space-y-4 text-gray-700 leading-7">
            <p>{post.content}</p>
          </div>
        </div>

        <!-- Disaster Details -->
        <div class="mt-10 border-t border-gray-200 pt-10">
          <h3 class="text-sm font-medium text-gray-900">Disaster Details</h3>
          <div class="prose prose-sm mt-4 text-gray-500">
            <ul role="list">
              <li><strong>Location:</strong> {post.location}</li>
              <li><strong>Reported:</strong> {new Date(post.reportedTime).toLocaleString()}</li>
              <li><strong>Category:</strong> {post.category}</li>
              <li><strong>Status:</strong> {post.status}</li>
            </ul>
          </div>
        </div>

        <!-- Emergency Contacts -->
        <div class="mt-10 border-t border-gray-200 pt-10">
          <h3 class="text-sm font-medium text-gray-900">Emergency Contacts</h3>
          <div class="prose prose-sm mt-4 text-gray-500">
            <ul role="list">
              {#each post.emergencyContacts as contact}
                <li>{contact}</li>
              {/each}
            </ul>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
