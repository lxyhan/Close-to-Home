<div class="flex min-h-screen bg-gray-50">
  <!-- Form Section -->
  <div class="flex flex-1 flex-col justify-center px-4 py-12 sm:px-6 lg:flex-none lg:px-20 xl:px-24">
    <div class="mx-auto w-full max-w-sm lg:w-96">
      <div>
        

        <div class="flex h-16 items-center space-x-4 px-0 mt-3">
          <!-- Replace SVG with an image -->
          <img 
            src="/logo.png" 
            alt="App Logo" 
            class="h-10 w-10 object-contain" 
          />
          
          <h1 class="text-2xl font-bold text-gray-900">Close to Home</h1>
        </div>
        
        <p class="mt-2 text-sm text-gray-500">
          Log in to explore live data and stay updated with alerts. 
          <a href="#" class="font-semibold text-indigo-600 hover:text-indigo-500">
            Create an account
          </a> for full access.
        </p>
      </div>

      <div class="mt-10">
        <!-- Login Form -->
        <form onsubmit={login(event)} class="space-y-6">
          <div>
            <label for="email" class="block text-sm font-medium text-gray-900">Email</label>
            <input
              id="email"
              type="text"
              placeholder="Enter any email"
              class="mt-2 block w-full rounded-md border py-1.5 shadow-sm ring-1 ring-gray-300 
                     focus:ring-2 focus:ring-indigo-600"
            />
          </div>

          <div>
            <label for="password" class="block text-sm font-medium text-gray-900">Password</label>
            <input
              id="password"
              type="password"
              placeholder="Enter any password"
              class="mt-2 block w-full rounded-md border py-1.5 shadow-sm ring-1 ring-gray-300 
                     focus:ring-2 focus:ring-indigo-600"
            />
          </div>

          <button
            type="submit"
            class="w-full rounded-md bg-indigo-600 px-3 py-2 text-white font-semibold hover:bg-indigo-500"
          >
            Sign in
          </button>
        </form>
      </div>
    </div>
  </div>

  <!-- Background Image Section -->
  <div class="relative hidden w-0 flex-1 lg:block">
    <img class="absolute inset-0 h-full w-full object-cover" src="/banner1.jpg" alt="Disaster Image" />
  </div>
</div>

<script>
  function login(event) {
    event.preventDefault(); // Prevent form submission from reloading the page
    window.location.href = "/dashboard"; // Redirect to dashboard
  }
</script>