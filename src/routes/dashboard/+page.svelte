<script>
  import MapboxMap from "../../components/MapboxMap.svelte";
	import Statistics from "../../components/Statistics.svelte";
  import Userlist from "../../components/Userlist.svelte";
  
  let currentState = 'map'; // Track if statistics modal is active

  export let username = 'James Han';

  function logout() {
    console.log('Logging out...');
    window.location.href = '/login'; // Redirect to login page
  }

  let accessToken = 'pk.eyJ1IjoiaGFubHl1MjAwNSIsImEiOiJjbTJxano5dWkxNXo0MmtxODM5MmxwN3lwIn0.2bgd33u52q49s2QcdaMVIg'; // Replace with your token

  const posts = [
  {
    title: 'Severe Flooding in New York City',
    slug: 'flooding-in-new-york',
    content:
      'Unprecedented flooding in Lower Manhattan has led to the evacuation of several neighborhoods. The subway system is halted, and rescue operations are underway. Please avoid the area and call 311 for non-emergency inquiries.',
    postImage: '/banner4.jpg',
    profileImage: '/pfp1.png',
    name: 'John Doe',
    location: 'New York, NY, USA',
    category: 'Flooding',
    reportedTime: '2 hours ago',
    status: 'Ongoing',
    emergencyContacts: ['311', 'NYC OEM'],
    lat: 40.7128, // New York City latitude
    lng: -74.0060, // New York City longitude
  },
  {
    title: 'California Wildfire Spreading Rapidly',
    slug: 'california-wildfire-spreading-rapidly',
    content:
      'A wildfire near San Bernardino has grown to over 10,000 acres. Evacuation orders are in effect for surrounding areas. Air quality is poor across the region, and residents are urged to stay indoors.',
    postImage: '/banner1.jpg',
    profileImage: '/pfp2.png',
    name: 'Jane Smith',
    location: 'San Bernardino, CA, USA',
    category: 'Wildfire',
    reportedTime: '1 hour ago',
    status: 'Evacuations Ongoing',
    emergencyContacts: ['911', 'Cal Fire'],
    lat: 34.1083, // San Bernardino latitude
    lng: -117.2898, // San Bernardino longitude
  },
  {
    title: 'Hurricane Laura Makes Landfall',
    slug: 'hurricane-laura-makes-landfall',
    content:
      'Hurricane Laura has hit Louisiana as a Category 4 storm, with winds exceeding 150 mph. Power outages have been reported in Lake Charles and nearby cities. Stay sheltered and avoid all unnecessary travel.',
    postImage: '/banner4.jpg',
    profileImage: '/pfp3.png',
    name: 'Emily Johnson',
    location: 'Lake Charles, LA, USA',
    category: 'Hurricane',
    reportedTime: '3 hours ago',
    status: 'Critical',
    emergencyContacts: ['911', 'FEMA'],
    lat: 30.2266, // Lake Charles latitude
    lng: -93.2174, // Lake Charles longitude
  },
  {
    title: 'Earthquake Hits Southern Japan',
    slug: 'earthquake-hits-southern-japan',
    content:
      'A magnitude 6.8 earthquake shook the southern islands of Japan. Aftershocks continue to be felt in the region, and tsunami warnings have been issued. No major casualties reported yet, but infrastructure damage is significant.',
    postImage: '/banner3.jpg',
    profileImage: '/pfp4.png',
    name: 'Hideo Takahashi',
    location: 'Kyushu, Japan',
    category: 'Earthquake',
    reportedTime: '30 minutes ago',
    status: 'Monitoring Aftershocks',
    emergencyContacts: ['119', 'Japan Meteorological Agency'],
    lat: 32.7503, // Kyushu latitude
    lng: 130.7417, // Kyushu longitude
  },
  {
    title: 'Tornado in Oklahoma Destroys Homes',
    slug: 'tornado-in-oklahoma-destroys-homes',
    content:
      'A large tornado has touched down in Moore, Oklahoma, destroying several homes and vehicles. Emergency responders are on the scene, and residents are being advised to take shelter immediately.',
    postImage: '/banner4.jpg',
    profileImage: '/pfp3.png',
    name: 'Mike Andrews',
    location: 'Moore, OK, USA',
    category: 'Tornado',
    reportedTime: '45 minutes ago',
    status: 'First Responders on Site',
    emergencyContacts: ['911', 'American Red Cross'],
    lat: 35.3395, // Moore latitude
    lng: -97.4867, // Moore longitude
  },
  {
    title: 'Massive Landslide in Northern India',
    slug: 'massive-landslide-in-northern-india',
    content:
      'A major landslide in the Himalayan region has blocked roads and caused multiple injuries. Rescue teams are struggling to reach remote villages affected by the landslide. Helicopters have been deployed for rescue.',
    postImage: '/banner3.jpg',
    profileImage: '/pfp2.png',
    name: 'Ravi Kumar',
    location: 'Himachal Pradesh, India',
    category: 'Landslide',
    reportedTime: '1 hour ago',
    status: 'Rescue Operations Underway',
    emergencyContacts: ['108', 'Disaster Management Authority'],
    lat: 31.1048, // Himachal Pradesh latitude
    lng: 77.1734, // Himachal Pradesh longitude
  },
  {
    title: 'Heatwave in Spain Leads to Health Alerts',
    slug: 'heatwave-in-spain-leads-to-health-alerts',
    content:
      'Spain is experiencing an extreme heatwave, with temperatures exceeding 45°C (113°F). Health authorities have issued alerts, urging residents to stay hydrated and avoid outdoor activities during peak hours.',
    postImage: '/banner2.jpg',
    profileImage: '/pfp1.png',
    name: 'Carlos Martinez',
    location: 'Seville, Spain',
    category: 'Heatwave',
    reportedTime: '2 days ago',
    status: 'Health Alert Issued',
    emergencyContacts: ['112', 'Spanish Red Cross'],
    lat: 37.3891, // Seville latitude
    lng: -5.9845, // Seville longitude
  },
  {
    title: 'Flash Floods in the Philippines',
    slug: 'flash-floods-in-the-philippines',
    content:
      'Heavy rainfall has caused flash floods across Manila, submerging roads and disrupting transportation. Evacuation centers are being set up, and residents are advised to move to higher ground.',
    postImage: '/banner1.jpg',
    profileImage: '/pfp2.png',
    name: 'Alyssa Reyes',
    location: 'Manila, Philippines',
    category: 'Flash Flood',
    reportedTime: '4 hours ago',
    status: 'Evacuations in Progress',
    emergencyContacts: ['911', 'Philippine Red Cross'],
    lat: 14.5995, // Manila latitude
    lng: 120.9842, // Manila longitude
  }
];


  let filteredPosts = [...posts]; // Default: show all posts
  let selectedPost = ''; // Track selected post

  function handleFilteredPosts(posts) {
    filteredPosts = posts; // Update user list
    selectedPost = posts.length ? posts[0].title : ''; // Update selected post title
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
                     src="https://tailwindui.com/plus/img/logos/mark.svg?color=indigo&shade=600" 
                     alt="ClimateWatch Logo" />
              
                <h1 class="text-2xl font-bold text-gray-900">ClimateWatch</h1>
            </div>              
            <nav class="flex flex-1 flex-col">
              <ul role="list" class="flex flex-1 flex-col gap-y-7">
                <li>
                  <ul role="list" class="-mx-2 space-y-1">
                    <li>
                      <!-- Current: "bg-gray-50 text-indigo-600", Default: "text-gray-700 hover:text-indigo-600 hover:bg-gray-50" -->
                      <a href="#" class="group flex gap-x-3 rounded-md bg-gray-50 p-2 text-sm font-semibold leading-6 text-indigo-600">
                        <svg class="h-6 w-6 shrink-0 text-indigo-600" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" aria-hidden="true" data-slot="icon">
                          <path stroke-linecap="round" stroke-linejoin="round" d="m2.25 12 8.954-8.955c.44-.439 1.152-.439 1.591 0L21.75 12M4.5 9.75v10.125c0 .621.504 1.125 1.125 1.125H9.75v-4.875c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21h4.125c.621 0 1.125-.504 1.125-1.125V9.75M8.25 21h8.25" />
                        </svg>
                        Dashboard
                      </a>
                    </li>
                    <li>
                      <a href="#" class="group flex gap-x-3 rounded-md p-2 text-sm font-semibold leading-6 text-gray-700 hover:bg-gray-50 hover:text-indigo-600">
                        <svg class="h-6 w-6 shrink-0 text-gray-400 group-hover:text-indigo-600" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" aria-hidden="true" data-slot="icon">
                          <path stroke-linecap="round" stroke-linejoin="round" d="M15 19.128a9.38 9.38 0 0 0 2.625.372 9.337 9.337 0 0 0 4.121-.952 4.125 4.125 0 0 0-7.533-2.493M15 19.128v-.003c0-1.113-.285-2.16-.786-3.07M15 19.128v.106A12.318 12.318 0 0 1 8.624 21c-2.331 0-4.512-.645-6.374-1.766l-.001-.109a6.375 6.375 0 0 1 11.964-3.07M12 6.375a3.375 3.375 0 1 1-6.75 0 3.375 3.375 0 0 1 6.75 0Zm8.25 2.25a2.625 2.625 0 1 1-5.25 0 2.625 2.625 0 0 1 5.25 0Z" />
                        </svg>
                        Team
                      </a>
                    </li>
                    <li>
                      <a href="#" class="group flex gap-x-3 rounded-md p-2 text-sm font-semibold leading-6 text-gray-700 hover:bg-gray-50 hover:text-indigo-600">
                        <svg class="h-6 w-6 shrink-0 text-gray-400 group-hover:text-indigo-600" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" aria-hidden="true" data-slot="icon">
                          <path stroke-linecap="round" stroke-linejoin="round" d="M15.75 17.25v3.375c0 .621-.504 1.125-1.125 1.125h-9.75a1.125 1.125 0 0 1-1.125-1.125V7.875c0-.621.504-1.125 1.125-1.125H6.75a9.06 9.06 0 0 1 1.5.124m7.5 10.376h3.375c.621 0 1.125-.504 1.125-1.125V11.25c0-4.46-3.243-8.161-7.5-8.876a9.06 9.06 0 0 0-1.5-.124H9.375c-.621 0-1.125.504-1.125 1.125v3.5m7.5 10.375H9.375a1.125 1.125 0 0 1-1.125-1.125v-9.25m12 6.625v-1.875a3.375 3.375 0 0 0-3.375-3.375h-1.5a1.125 1.125 0 0 1-1.125-1.125v-1.5a3.375 3.375 0 0 0-3.375-3.375H9.75" />
                        </svg>
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

        <div class="flex h-16 items-center space-x-4 px-4 mt-3">
            <svg id="logo-86" width="40" height="40" viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg"><path class="ccustom" fill-rule="evenodd" clip-rule="evenodd" d="M25.5557 11.6853C23.9112 10.5865 21.9778 10 20 10V0C23.9556 0 27.8224 1.17298 31.1114 3.37061C34.4004 5.56823 36.9638 8.69181 38.4776 12.3463C39.9913 16.0008 40.3874 20.0222 39.6157 23.9018C38.844 27.7814 36.9392 31.3451 34.1421 34.1421C31.3451 36.9392 27.7814 38.844 23.9018 39.6157C20.0222 40.3874 16.0008 39.9913 12.3463 38.4776C8.69181 36.9638 5.56823 34.4004 3.37061 31.1114C1.17298 27.8224 0 23.9556 0 20H10C10 21.9778 10.5865 23.9112 11.6853 25.5557C12.7841 27.2002 14.3459 28.4819 16.1732 29.2388C18.0004 29.9957 20.0111 30.1937 21.9509 29.8078C23.8907 29.422 25.6725 28.4696 27.0711 27.0711C28.4696 25.6725 29.422 23.8907 29.8078 21.9509C30.1937 20.0111 29.9957 18.0004 29.2388 16.1732C28.4819 14.3459 27.2002 12.7841 25.5557 11.6853Z" fill="#007DFC"></path><path class="ccustom" fill-rule="evenodd" clip-rule="evenodd" d="M10 5.16562e-07C10 1.31322 9.74135 2.61358 9.2388 3.82683C8.73625 5.04009 7.99966 6.14248 7.07107 7.07107C6.14249 7.99966 5.0401 8.73625 3.82684 9.2388C2.61358 9.74134 1.31322 10 5.4439e-06 10L5.00679e-06 20C2.62644 20 5.22716 19.4827 7.65368 18.4776C10.0802 17.4725 12.285 15.9993 14.1421 14.1421C15.9993 12.285 17.4725 10.0802 18.4776 7.65367C19.4827 5.22715 20 2.62643 20 -3.81469e-06L10 5.16562e-07Z" fill="#007DFC"></path></svg>
            <h1 class="text-2xl font-bold text-gray-900">ClimateWatch</h1>
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
                      <svg class="h-6 w-6 shrink-0 {currentState === 'disasters' ? 'text-indigo-600' : 'text-gray-400 group-hover:text-indigo-600'}" 
                        fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" aria-hidden="true">
                        <path stroke-linecap="round" stroke-linejoin="round" d="m2.25 12 8.954-8.955c.44-.439 1.152-.439 1.591 0L21.75 12M4.5 9.75v10.125c0 .621.504 1.125 1.125 1.125H9.75v-4.875c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21h4.125c.621 0 1.125-.504 1.125-1.125V9.75M8.25 21h8.25" />
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
                      <svg class="h-6 w-6 shrink-0 {currentState === 'heatmap' ? 'text-indigo-600' : 'text-gray-400 group-hover:text-indigo-600'}" 
                        fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" aria-hidden="true">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M15 19.128a9.38 9.38 0 0 0 2.625.372 9.337 9.337 0 0 0 4.121-.952 4.125 4.125 0 0 0-7.533-2.493M15 19.128v-.003c0-1.113-.285-2.16-.786-3.07M15 19.128v.106A12.318 12.318 0 0 1 8.624 21c-2.331 0-4.512-.645-6.374-1.766l-.001-.109a6.375 6.375 0 0 1 11.964-3.07M12 6.375a3.375 3.375 0 1 1-6.75 0 3.375 3.375 0 0 1 6.75 0Zm8.25 2.25a2.625 2.625 0 1 1-5.25 0 2.625 2.625 0 0 1 5.25 0Z" />
                      </svg>
                      Heatmap
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
                      <svg class="h-6 w-6 shrink-0 {currentState === 'stats' ? 'text-indigo-600' : 'text-gray-400 group-hover:text-indigo-600'}" 
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
              <div class="text-xs font-semibold leading-6 text-gray-400">Saved Locations</div>
              <ul role="list" class="-mx-2 mt-2 space-y-1">
                <li>
                  <!-- Current: "bg-gray-50 text-indigo-600", Default: "text-gray-700 hover:text-indigo-600 hover:bg-gray-50" -->
                  <a href="#" class="group flex gap-x-3 rounded-md p-2 text-sm font-semibold leading-6 text-gray-700 hover:bg-gray-50 hover:text-indigo-600">
                    <span class="flex h-6 w-6 shrink-0 items-center justify-center rounded-lg border border-gray-200 bg-white text-[0.625rem] font-medium text-gray-400 group-hover:border-indigo-600 group-hover:text-indigo-600">H</span>
                    <button on:click={() => handleMapClick('New York')}>New York</button>
                  </a>
                </li>
                <li>
                    <!-- Current: "bg-gray-50 text-indigo-600", Default: "text-gray-700 hover:text-indigo-600 hover:bg-gray-50" -->
                    <a href="#" class="group flex gap-x-3 rounded-md p-2 text-sm font-semibold leading-6 text-gray-700 hover:bg-gray-50 hover:text-indigo-600">
                      <span class="flex h-6 w-6 shrink-0 items-center justify-center rounded-lg border border-gray-200 bg-white text-[0.625rem] font-medium text-gray-400 group-hover:border-indigo-600 group-hover:text-indigo-600">H</span>
                      <span class="truncate">Chengdu</span>
                    </a>
                  </li>
                  <li>
                    <!-- Current: "bg-gray-50 text-indigo-600", Default: "text-gray-700 hover:text-indigo-600 hover:bg-gray-50" -->
                    <a href="#" class="group flex gap-x-3 rounded-md p-2 text-sm font-semibold leading-6 text-gray-700 hover:bg-gray-50 hover:text-indigo-600">
                      <span class="flex h-6 w-6 shrink-0 items-center justify-center rounded-lg border border-gray-200 bg-white text-[0.625rem] font-medium text-gray-400 group-hover:border-indigo-600 group-hover:text-indigo-600">H</span>
                      <span class="truncate">Mumbai</span>
                    </a>
                  </li>
              </ul>
            </li>
            <li class="-mx-6 mt-auto">
                <button 
                  class="flex w-full items-center gap-x-4 px-6 py-3 text-sm font-semibold leading-6 text-gray-900 hover:bg-gray-50"
                  on:click={() => logout()}
                >
                <img 
                class="h-8 w-8 rounded-full bg-gray-50 object-cover" 
                src="/IMG_9453.jpg" 
                alt={username}
              />
              
                  <span class="sr-only">Your profile</span>
                  <span aria-hidden="true">{username}</span>
                </button>
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
              {:else}
                <MapboxMap {posts} {accessToken} onFilterPosts={handleFilteredPosts} />
              {/if}
          </div>
        </div>
      </div>
    </main>
  
    <aside class="fixed inset-y-0 left-72 hidden w-96 overflow-y-auto border-r border-gray-200 px-4 py-6 sm:px-6 lg:px-8 xl:block">
      <Userlist {posts} {selectedPost} />
    </aside>

  </div>