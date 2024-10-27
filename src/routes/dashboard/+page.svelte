<script>
	import AddPostModal from "../../components/AddPostModal.svelte";
	import Heatmap from "../../components/Heatmap.svelte";
  import MapboxMap from "../../components/MapboxMap.svelte";
	import Statistics from "../../components/Statistics.svelte";
	import StreetLevelMap from "../../components/StreetLevelMap.svelte";
  import Userlist from "../../components/Userlist.svelte";
  
  let currentState = 'map'; // Track if statistics modal is active
  let openAddPostModal = false;

  export let username = 'James Han';

  function logout() {
    console.log('Logging out...');
    window.location.href = '/login'; // Redirect to login page
  }

  let accessToken = 'pk.eyJ1IjoiaGFubHl1MjAwNSIsImEiOiJjbTJxano5dWkxNXo0MmtxODM5MmxwN3lwIn0.2bgd33u52q49s2QcdaMVIg'; // Replace with your token

  let posts = [
  {
    title: 'Flooding in New York Traps Residents',
    slug: 'flooding-in-nyc',
    content:
      'Heavy rains have caused severe flooding across several neighborhoods in Brooklyn. Many families are stuck in their homes, and the water levels are rising. We need boats and clean drinking water.',
    postImage: '/flood.jpg',
    profileImage: '/pfp1.png',
    name: 'John Hancock',
    location: 'Brooklyn, NY, USA',
    category: 'Flooding',
    reportedTime: '3 hours ago',
    status: 'Rescue Needed',
    emergencyContacts: ['311', 'NYC OEM'],
    donationRequests: ['Water', 'Boats', 'Non-perishable food'],
    lat: 40.6782,
    lng: -73.9442,
  },
  {
    title: 'Earthquake Aftermath in Turkey',
    slug: 'earthquake-in-turkey',
    content:
      'A devastating 7.2-magnitude earthquake struck eastern Turkey, destroying homes and schools. Survivors urgently need tents, blankets, and medical kits.',
    postImage: '/earthquake.jpeg',
    profileImage: '/pfp2.png',
    name: 'Ali Yilmaz',
    location: 'Van, Turkey',
    category: 'Earthquake',
    reportedTime: '5 hours ago',
    status: 'Critical',
    emergencyContacts: ['112', 'AFAD'],
    donationRequests: ['Tents', 'Medical kits', 'Blankets'],
    lat: 38.5012,
    lng: 43.3790,
  },
  {
    title: 'Typhoon Haikui Wrecks Coastal Villages',
    slug: 'typhoon-haikui-in-philippines',
    content:
      'Typhoon Haikui has destroyed fishing villages along the coast, leaving many families homeless. We urgently need clothes, shelter, and food supplies.',
    postImage: '/banner5.jpg',
    profileImage: '/pfp3.png',
    name: 'Lina Santos',
    location: 'Palawan, Philippines',
    category: 'Typhoon',
    reportedTime: '2 hours ago',
    status: 'Displacement Ongoing',
    emergencyContacts: ['911', 'Philippine Red Cross'],
    donationRequests: ['Clothing', 'Food', 'Temporary shelters'],
    lat: 9.7392,
    lng: 118.7353,
  },
  {
    title: 'Wildfire Evacuees Need Supplies',
    slug: 'wildfire-in-oregon',
    content:
      'Evacuees from the massive wildfire in Oregon are now in shelters, running out of essential supplies. We need hygiene kits and pet food for displaced animals.',
    postImage: '/banner1.jpg',
    profileImage: '/pfp4.png',
    name: 'Sarah Thompson',
    location: 'Bend, OR, USA',
    category: 'Wildfire',
    reportedTime: '6 hours ago',
    status: 'Shelters Overcrowded',
    emergencyContacts: ['911', 'Oregon Fire Department'],
    donationRequests: ['Hygiene kits', 'Baby formula', 'Pet food'],
    lat: 44.0582,
    lng: -121.3153,
  },
  {
    title: 'Tornado in Texas Causes Power Outage',
    slug: 'tornado-in-texas',
    content:
      'A powerful tornado struck the outskirts of Dallas, leaving thousands without power. Families need generators and food supplies.',
    postImage: '/banner2.jpg',
    profileImage: '/pfp1.png',
    name: 'Mark Wilson',
    location: 'Dallas, TX, USA',
    category: 'Tornado',
    reportedTime: '1 hour ago',
    status: 'Ongoing Rescue',
    emergencyContacts: ['911', 'Texas Emergency Services'],
    donationRequests: ['Generators', 'Food packs', 'Flashlights'],
    lat: 32.7767,
    lng: -96.7970,
  },
  {
    title: 'Hurricane Ian Floods Florida Towns',
    slug: 'hurricane-ian-floods-florida',
    content:
      'Hurricane Ian has flooded streets and homes across Fort Myers. Many people are stranded, and shelters are running out of supplies.',
    postImage: '/banner6.jpg',
    profileImage: '/pfp2.png',
    name: 'Emma Brown',
    location: 'Fort Myers, FL, USA',
    category: 'Hurricane',
    reportedTime: '8 hours ago',
    status: 'Emergency',
    emergencyContacts: ['911', 'FEMA'],
    donationRequests: ['Life vests', 'Medicines', 'Blankets'],
    lat: 26.6406,
    lng: -81.8723,
  },
  {
    title: 'Flash Floods in Malaysia Submerge Towns',
    slug: 'flash-flood-in-malaysia',
    content:
      'Heavy rains have caused flash floods in Johor. Residents are stranded without food and clean water. We need help urgently.',
    postImage: '/banner7.jpg',
    profileImage: '/pfp3.png',
    name: 'Muhammad Iqbal',
    location: 'Johor, Malaysia',
    category: 'Flash Flood',
    reportedTime: '2 hours ago',
    status: 'Rescue Operations Ongoing',
    emergencyContacts: ['999', 'Malaysia Civil Defence Force'],
    donationRequests: ['Clean water', 'Food supplies', 'Dry clothes'],
    lat: 1.4927,
    lng: 103.7414,
  },
  {
    title: 'Volcanic Eruption in Indonesia',
    slug: 'volcano-in-indonesia',
    content:
      'Mount Sinabung has erupted, covering villages in ash. Thousands have evacuated, but we need respirators, food, and shelter urgently.',
    postImage: '/banner3.jpg',
    profileImage: '/pfp4.png',
    name: 'Putri Ananda',
    location: 'Karo, Indonesia',
    category: 'Volcano Eruption',
    reportedTime: '1 hour ago',
    status: 'Critical',
    emergencyContacts: ['112', 'Indonesian Red Cross'],
    donationRequests: ['Respirators', 'Food', 'Shelter tents'],
    lat: 3.1741,
    lng: 98.3923,
  },
  {
    title: 'Blizzard in Canada Traps Travelers',
    slug: 'blizzard-in-canada',
    content:
      'A sudden blizzard in Saskatchewan has stranded travelers on highways. Many are without fuel and supplies, seeking assistance.',
    postImage: '/blizzard.jpeg',
    profileImage: '/pfp1.png',
    name: 'James White',
    location: 'Saskatchewan, Canada',
    category: 'Blizzard',
    reportedTime: '30 minutes ago',
    status: 'Emergency Services Dispatched',
    emergencyContacts: ['911', 'Canadian Red Cross'],
    donationRequests: ['Fuel', 'Warm clothing', 'First aid kits'],
    lat: 52.9399,
    lng: -106.4509,
  },
  {
    title: 'Monsoon Floods Worsen in Bangladesh',
    slug: 'monsoon-floods-in-bangladesh',
    content:
      'Monsoon rains have caused rivers to overflow, flooding villages in Sylhet. We are trapped and need help with food, medicine, and rescue boats.',
    postImage: '/banner6.jpg',
    profileImage: '/pfp2.png',
    name: 'Amina Rahman',
    location: 'Sylhet, Bangladesh',
    category: 'Monsoon Flood',
    reportedTime: '12 hours ago',
    status: 'Rescue Needed',
    emergencyContacts: ['999', 'Bangladesh Red Crescent'],
    donationRequests: ['Boats', 'Medicine', 'Food'],
    lat: 24.8949,
    lng: 91.8687,
  }
];


  let filteredPosts = [...posts]; // Default: show all posts
  let selectedPost = ''; // Track selected post

  function handleFilteredPosts(posts) {
    filteredPosts = posts; // Update user list
    selectedPost = posts.length ? posts[0].title : ''; // Update selected post title
  }

  function openModal() {
    openAddPostModal = true;
  }

  function closeModal() {
    openAddPostModal = false;
  }

  function savePost(newPost) {
    posts = [...posts, newPost]; // Add the new post to the list
  }

</script>
<!--
  This example requires updating your template:

  ```
  <html class="h-full bg-white">
  <body class="h-full">
  ```
-->
<div>
    <!-- Off-canvas menu for mobile, show/hide based on off-canvas menu state. -->
    <div class="relative z-50 lg:hidden" role="dialog" aria-modal="true">
      <!--
        Off-canvas menu backdrop, show/hide based on off-canvas menu state.
  
        Entering: "transition-opacity ease-linear duration-300"
          From: "opacity-0"
          To: "opacity-100"
        Leaving: "transition-opacity ease-linear duration-300"
          From: "opacity-100"
          To: "opacity-0"
      -->
      <div class="fixed inset-0 bg-gray-900/80" aria-hidden="true"></div>
  
      <div class="fixed inset-0 flex">
        <!--
          Off-canvas menu, show/hide based on off-canvas menu state.
  
          Entering: "transition ease-in-out duration-300 transform"
            From: "-translate-x-full"
            To: "translate-x-0"
          Leaving: "transition ease-in-out duration-300 transform"
            From: "translate-x-0"
            To: "-translate-x-full"
        -->
        <div class="relative mr-16 flex w-full max-w-xs flex-1">
          <!--
            Close button, show/hide based on off-canvas menu state.
  
            Entering: "ease-in-out duration-300"
              From: "opacity-0"
              To: "opacity-100"
            Leaving: "ease-in-out duration-300"
              From: "opacity-100"
              To: "opacity-0"
          -->
          <div class="absolute left-full top-0 flex w-16 justify-center pt-5">
            <button type="button" class="-m-2.5 p-2.5">
              <span class="sr-only">Close sidebar</span>
              <svg class="h-6 w-6 text-white" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" aria-hidden="true" data-slot="icon">
                <path stroke-linecap="round" stroke-linejoin="round" d="M6 18 18 6M6 6l12 12" />
              </svg>
            </button>
          </div>
  
          <!-- Sidebar component, swap this element with another sidebar if you like -->
          <div class="flex grow flex-col gap-y-5 overflow-y-auto bg-white px-6 pb-2">
            <div class="flex h-16 items-center space-x-4 px-4">
                <img class="h-8 w-auto" 
                     src="/logo.png" 
                     alt="ClimateWatch Logo" />
              
                <h1 class="text-2xl font-bold text-gray-900">Close to Home</h1>
            </div>              
            <nav class="flex flex-1 flex-col">
              <ul role="list" class="flex flex-1 flex-col gap-y-7">
                <li>
                  <ul role="list" class="-mx-2 space-y-1">
                    <li>
                      <!-- Current: "bg-gray-50 text-indigo-600", Default: "text-gray-700 hover:text-indigo-600 hover:bg-gray-50" -->
                      <a href="#" class="group flex gap-x-3 rounded-md bg-gray-50 p-2 text-sm font-semibold leading-6 text-indigo-600">

                        Dashboard
                      </a>
                    </li>
                    <li>
                      <a href="#" class="group flex gap-x-3 rounded-md p-2 text-sm font-semibold leading-6 text-gray-700 hover:bg-gray-50 hover:text-indigo-600">

                        Team
                      </a>
                    </li>
                    <li>
                      <a href="#" class="group flex gap-x-3 rounded-md p-2 text-sm font-semibold leading-6 text-gray-700 hover:bg-gray-50 hover:text-indigo-600">

                        Documents
                      </a>
                    </li>
                    <li>
                      <a href="#" class="group flex gap-x-3 rounded-md p-2 text-sm font-semibold leading-6 text-gray-700 hover:bg-gray-50 hover:text-indigo-600">
                        <svg class="h-6 w-6 shrink-0 text-gray-400 group-hover:text-indigo-600" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" aria-hidden="true" data-slot="icon">
                          <path stroke-linecap="round" stroke-linejoin="round" d="M10.5 6a7.5 7.5 0 1 0 7.5 7.5h-7.5V6Z" />
                          <path stroke-linecap="round" stroke-linejoin="round" d="M13.5 10.5H21A7.5 7.5 0 0 0 13.5 3v7.5Z" />
                        </svg>
                        Reports
                      </a>
                    </li>
                  </ul>
                </li>
                <li>
                  <div class="text-xs font-semibold leading-6 text-gray-400">Your teams</div>
                  <ul role="list" class="-mx-2 mt-2 space-y-1">
                    <li>
                      <!-- Current: "bg-gray-50 text-indigo-600", Default: "text-gray-700 hover:text-indigo-600 hover:bg-gray-50" -->
                      <a href="#" class="group flex gap-x-3 rounded-md p-2 text-sm font-semibold leading-6 text-gray-700 hover:bg-gray-50 hover:text-indigo-600">
                        <span class="flex h-6 w-6 shrink-0 items-center justify-center rounded-lg border border-gray-200 bg-white text-[0.625rem] font-medium text-gray-400 group-hover:border-indigo-600 group-hover:text-indigo-600">H</span>
                        <span class="truncate">Heroicons</span>
                      </a>
                    </li>
                    <li>
                      <a href="#" class="group flex gap-x-3 rounded-md p-2 text-sm font-semibold leading-6 text-gray-700 hover:bg-gray-50 hover:text-indigo-600">
                        <span class="flex h-6 w-6 shrink-0 items-center justify-center rounded-lg border border-gray-200 bg-white text-[0.625rem] font-medium text-gray-400 group-hover:border-indigo-600 group-hover:text-indigo-600">T</span>
                        <span class="truncate">Tailwind Labs</span>
                      </a>
                    </li>
                    <li>
                      <a href="#" class="group flex gap-x-3 rounded-md p-2 text-sm font-semibold leading-6 text-gray-700 hover:bg-gray-50 hover:text-indigo-600">
                        <span class="flex h-6 w-6 shrink-0 items-center justify-center rounded-lg border border-gray-200 bg-white text-[0.625rem] font-medium text-gray-400 group-hover:border-indigo-600 group-hover:text-indigo-600">W</span>
                        <span class="truncate">Workcation</span>
                      </a>
                    </li>
                  </ul>
                </li>
              </ul>
            </nav>
          </div>
        </div>
      </div>
    </div>
  
    <!-- Static sidebar for desktop -->
    <div class="hidden lg:fixed lg:inset-y-0 lg:z-50 lg:flex lg:w-72 lg:flex-col">
      <!-- Sidebar component, swap this element with another sidebar if you like -->
      <div class="flex grow flex-col gap-y-5 overflow-y-auto border-r border-gray-200 bg-white px-6">

        <div class="flex h-16 items-center space-x-1 px-0 mt-3">
          <img 
            src="/logo.png" 
            alt="App Logo" 
            class="h-12 w-12 object-cover rounded-full"
          />
            <h1 class="text-2xl font-bold text-gray-900">Close to Home</h1>
        </div>

        <nav class="flex flex-1 flex-col">
          <ul role="list" class="flex flex-1 flex-col gap-y-7">
            <li>
              <ul role="list" class="-mx-2 space-y-1">
                <li>
                    <a 
                      href="#" 
                      class="group flex gap-x-3 rounded-md p-2 text-sm font-semibold leading-6 
                        {currentState === 'disasters' ? 'bg-gray-200 text-indigo-600' : 'text-gray-700 hover:bg-gray-50 hover:text-indigo-600'}"
                      on:click={(e) => { 
                        e.preventDefault(); 
                        currentState = 'disasters'; 
                      }}
                    >
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="size-6">
                      <path stroke-linecap="round" stroke-linejoin="round" d="M15 10.5a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z" />
                      <path stroke-linecap="round" stroke-linejoin="round" d="M19.5 10.5c0 7.142-7.5 11.25-7.5 11.25S4.5 17.642 4.5 10.5a7.5 7.5 0 1 1 15 0Z" />
                    </svg>
                    

                      Disaster Areas
                    </a>
                  </li>
                  
                  <li>
                    <a 
                      href="#" 
                      class="group flex gap-x-3 rounded-md p-2 text-sm font-semibold leading-6 
                        {currentState === 'heatmap' ? 'bg-gray-200 text-indigo-600' : 'text-gray-700 hover:bg-gray-50 hover:text-indigo-600'}"
                      on:click={(e) => { 
                        e.preventDefault(); 
                        currentState = 'heatmap'; 
                      }}
                    >
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="size-6">
                      <path stroke-linecap="round" stroke-linejoin="round" d="M9 6.75V15m6-6v8.25m.503 3.498 4.875-2.437c.381-.19.622-.58.622-1.006V4.82c0-.836-.88-1.38-1.628-1.006l-3.869 1.934c-.317.159-.69.159-1.006 0L9.503 3.252a1.125 1.125 0 0 0-1.006 0L3.622 5.689C3.24 5.88 3 6.27 3 6.695V19.18c0 .836.88 1.38 1.628 1.006l3.869-1.934c.317-.159.69-.159 1.006 0l4.994 2.497c.317.158.69.158 1.006 0Z" />
                    </svg>

                      ML Damage Assessment Heatmap
                    </a>
                  </li>

                  <li>
                    <a 
                      href="#" 
                      class="group flex gap-x-3 rounded-md p-2 text-sm font-semibold leading-6 
                        {currentState === '3Dmap' ? 'bg-gray-200 text-indigo-600' : 'text-gray-700 hover:bg-gray-50 hover:text-indigo-600'}"
                      on:click={(e) => { 
                        e.preventDefault(); 
                        currentState = '3Dmap'; 
                      }}
                    >

                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="size-6">
                      <path stroke-linecap="round" stroke-linejoin="round" d="m21 21-5.197-5.197m0 0A7.5 7.5 0 1 0 5.196 5.196a7.5 7.5 0 0 0 10.607 10.607ZM10.5 7.5v6m3-3h-6" />
                    </svg>
                    
                    

                      Street Level Map
                    </a>
                  </li>
                  
                  <li>
                    <a 
                      href="#" 
                      class="group flex gap-x-3 rounded-md p-2 text-sm font-semibold leading-6 
                        {currentState === 'stats' ? 'bg-gray-200 text-indigo-600' : 'text-gray-700 hover:bg-gray-50 hover:text-indigo-600'}"
                      on:click={(e) => { 
                        e.preventDefault(); 
                        currentState = 'stats'; 
                      }}
                    >
                      <svg class="h-6 w-6 shrink-0 {currentState === 'stats' ? 'text-indigo-600' : 'text-gray-700 group-hover:text-indigo-600'}" 
                        fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" aria-hidden="true">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M10.5 6a7.5 7.5 0 1 0 7.5 7.5h-7.5V6Z" />
                        <path stroke-linecap="round" stroke-linejoin="round" d="M13.5 10.5H21A7.5 7.5 0 0 0 13.5 3v7.5Z" />
                      </svg>
                      Statistics
                    </a>
                </li>

              </ul>
            </li>
            <li>
              <div class="text-xs font-semibold leading-6 text-gray-400">More Actions</div>
              <ul role="list" class="-mx-2 mt-2 space-y-1">
                <li>
                  <a
                    href="#"
                    class="group flex gap-x-3 mb-2 rounded-md p-2 text-sm font-semibold leading-6 text-gray-700 hover:bg-gray-50 hover:text-indigo-600"
                    on:click|preventDefault={openModal}
                  >
                    <span
                      class="flex h-6 w-6 shrink-0 items-center justify-center rounded-lg border border-gray-700 bg-white text-[0.625rem] font-medium text-gray-700 group-hover:border-indigo-600 group-hover:text-indigo-600"
                    >
                      +
                    </span>
                    <button>Add a Post</button>
                  </a>
                </li>
                <div class="flex justify-center mx-2 mt-">
                  <!-- Donation Button -->
                  <button 
                    type="button" 
                    on:click={() => window.location.href="https://dashboard.stripe.com/"} 
                    class="block w-full max-w-xs rounded-lg border-2 border-dashed border-gray-300 p-6 text-center hover:border-gray-400 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2"
                  >
                    <div class="flex flex-col items-center space-y-2">
                      <img 
                        src="/m_logo.png" 
                        alt="Donation Icon" 
                      />
                      <span class="block text-sm font-semibold text-gray-900">
                        Create a donation endpoint
                      </span>
                    </div>
                  </button>
                </div>
                
                
                
                
              </ul>
            </li>
            <script>
              let username = "John Doe"; // Example username
            
              function logout() {
                // Add your logout logic here
                console.log("User logged out");
                // For example: Clear auth tokens, redirect to login page, etc.
              }
            </script>
            
            <li class="-mx-6 mt-auto">
              <div class="flex w-full items-center gap-x-4 px-6 py-3 text-sm font-semibold leading-6 text-gray-900 hover:bg-gray-50">
                <img 
                  class="h-8 w-8 rounded-full bg-gray-50 object-cover" 
                  src="/IMG_9453.jpg" 
                  alt={username}
                />
            
                <span aria-hidden="true">{username}</span>
            
                <!-- Logout Button -->
                <button 
                  class="ml-auto px-3 py-1 text-sm font-medium text-white bg-red-500 hover:bg-red-600 rounded-md"
                  on:click={logout}
                >
                  Logout
                </button>
              </div>
            </li>
            
              
          </ul>
        </nav>
      </div>
    </div>
  
    <div class="sticky top-0 z-40 flex items-center gap-x-6 bg-white px-4 py-4 shadow-sm sm:px-6 lg:hidden">
      <button type="button" class="-m-2.5 p-2.5 text-gray-700 lg:hidden">
        <span class="sr-only">Open sidebar</span>
        <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" aria-hidden="true" data-slot="icon">
          <path stroke-linecap="round" stroke-linejoin="round" d="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25h16.5" />
        </svg>
      </button>
      <div class="flex-1 text-sm font-semibold leading-6 text-gray-900">Dashboard</div>
      <a href="#">
        <span class="sr-only">Your profile</span>
        <img class="h-8 w-8 rounded-full bg-gray-50" src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
      </a>
    </div>
  
    <main class="lg:pl-72 h-screen">
      <div class="xl:pl-96 h-full">
        <div class="px-4 py-10 sm:px-6 lg:px-8 lg:py-6 h-full">
          <!-- Main area -->
          <div class="relative h-full w-full">
              {#if currentState == 'stats'}
                <Statistics {posts}></Statistics>
              {:else if currentState == '3Dmap'}
                <StreetLevelMap {posts} {accessToken} onFilterPosts={handleFilteredPosts}></StreetLevelMap>
              {:else if currentState == 'heatmap'}
                <Heatmap {posts}></Heatmap>
              {:else}
                <MapboxMap {posts} {accessToken} onFilterPosts={handleFilteredPosts} />
              {/if}
              <AddPostModal open={openAddPostModal} onSave={savePost} onClose={closeModal} />

          </div>
        </div>
      </div>
    </main>
  
    <aside class="fixed inset-y-0 left-72 hidden w-96 overflow-y-auto border-r border-gray-200 px-4 py-6 sm:px-6 lg:px-8 xl:block">
      <Userlist {posts} {selectedPost} />

    </aside>

  </div>