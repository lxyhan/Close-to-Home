<div class="flex min-h-screen bg-gray-50">
  <!-- Form Section -->
  <div class="flex flex-1 flex-col justify-center px-4 py-12 sm:px-6 lg:flex-none lg:px-20 xl:px-24">
    <div class="mx-auto w-full max-w-sm lg:w-96">
      <div>
        

        <div class="flex h-16 items-center space-x-4 px-0 mt-3">
          <svg id="logo-86" width="40" height="40" viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg"><path class="ccustom" fill-rule="evenodd" clip-rule="evenodd" d="M25.5557 11.6853C23.9112 10.5865 21.9778 10 20 10V0C23.9556 0 27.8224 1.17298 31.1114 3.37061C34.4004 5.56823 36.9638 8.69181 38.4776 12.3463C39.9913 16.0008 40.3874 20.0222 39.6157 23.9018C38.844 27.7814 36.9392 31.3451 34.1421 34.1421C31.3451 36.9392 27.7814 38.844 23.9018 39.6157C20.0222 40.3874 16.0008 39.9913 12.3463 38.4776C8.69181 36.9638 5.56823 34.4004 3.37061 31.1114C1.17298 27.8224 0 23.9556 0 20H10C10 21.9778 10.5865 23.9112 11.6853 25.5557C12.7841 27.2002 14.3459 28.4819 16.1732 29.2388C18.0004 29.9957 20.0111 30.1937 21.9509 29.8078C23.8907 29.422 25.6725 28.4696 27.0711 27.0711C28.4696 25.6725 29.422 23.8907 29.8078 21.9509C30.1937 20.0111 29.9957 18.0004 29.2388 16.1732C28.4819 14.3459 27.2002 12.7841 25.5557 11.6853Z" fill="#007DFC"></path><path class="ccustom" fill-rule="evenodd" clip-rule="evenodd" d="M10 5.16562e-07C10 1.31322 9.74135 2.61358 9.2388 3.82683C8.73625 5.04009 7.99966 6.14248 7.07107 7.07107C6.14249 7.99966 5.0401 8.73625 3.82684 9.2388C2.61358 9.74134 1.31322 10 5.4439e-06 10L5.00679e-06 20C2.62644 20 5.22716 19.4827 7.65368 18.4776C10.0802 17.4725 12.285 15.9993 14.1421 14.1421C15.9993 12.285 17.4725 10.0802 18.4776 7.65367C19.4827 5.22715 20 2.62643 20 -3.81469e-06L10 5.16562e-07Z" fill="#007DFC"></path></svg>
          <h1 class="text-2xl font-bold text-gray-900">ClimateWatch</h1>
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