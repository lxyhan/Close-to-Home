<script>
    import { onMount } from 'svelte';
    import Chart from 'chart.js/auto';
  
    let charts = {};
  
    let posts = [
  // USA
  { title: 'Flooding in New York', country: 'USA', category: 'Flooding', status: 'Rescue Needed', reportedAt: '2024-10-24' },
  { title: 'Wildfire in Oregon', country: 'USA', category: 'Wildfire', status: 'Shelters Overcrowded', reportedAt: '2024-10-22' },
  { title: 'Tornado in Texas', country: 'USA', category: 'Tornado', status: 'Ongoing Rescue', reportedAt: '2024-10-25' },
  { title: 'Tornado in Texas', country: 'USA', category: 'Tornado', status: 'Ongoing Rescue', reportedAt: '2024-10-25' },
  { title: 'Tornado in Texas', country: 'USA', category: 'Tornado', status: 'Ongoing Rescue', reportedAt: '2024-10-25' },

  // Turkey
  { title: 'Earthquake Aftermath in Turkey', country: 'Turkey', category: 'Earthquake', status: 'Critical', reportedAt: '2024-10-23' },
  { title: 'Aftershocks in Istanbul', country: 'Turkey', category: 'Earthquake', status: 'Monitoring Aftershocks', reportedAt: '2024-10-24' },
  { title: 'Aftershocks in Istanbul', country: 'Turkey', category: 'Earthquake', status: 'Monitoring Aftershocks', reportedAt: '2024-10-24' },

  // Philippines
  { title: 'Typhoon Haikui Wrecks Villages', country: 'Philippines', category: 'Typhoon', status: 'Displacement Ongoing', reportedAt: '2024-10-23' },
  { title: 'Flash Floods in Manila', country: 'Philippines', category: 'Flash Flood', status: 'Rescue Operations Ongoing', reportedAt: '2024-10-24' },

  // Canada
  { title: 'Blizzard in Canada', country: 'Canada', category: 'Blizzard', status: 'Emergency Services Dispatched', reportedAt: '2024-10-25' },
  { title: 'Avalanche Warning in Alberta', country: 'Canada', category: 'Avalanche', status: 'Warning Issued', reportedAt: '2024-10-23' },

  // Bangladesh
  { title: 'Monsoon Floods in Bangladesh', country: 'Bangladesh', category: 'Monsoon Flood', status: 'Rescue Needed', reportedAt: '2024-10-23' },
  { title: 'Flash Floods in Dhaka', country: 'Bangladesh', category: 'Flash Flood', status: 'Evacuations Ongoing', reportedAt: '2024-10-24' },

  // Indonesia
  { title: 'Volcano Eruption in Indonesia', country: 'Indonesia', category: 'Volcano Eruption', status: 'Critical', reportedAt: '2024-10-20' },
  { title: 'Ashfall from Mount Merapi', country: 'Indonesia', category: 'Volcano Eruption', status: 'Ashfall Warning', reportedAt: '2024-10-24' },

  // Spain
  { title: 'Forest Fires in Valencia', country: 'Spain', category: 'Wildfire', status: 'Under Control', reportedAt: '2024-10-24' },

  // Japan
  { title: 'Typhoon Jebi Hits Okinawa', country: 'Japan', category: 'Typhoon', status: 'Emergency Alert', reportedAt: '2024-10-23' },
];


  
    // Aggregate reports by date
    const reportsByDate = posts.reduce((acc, post) => {
      acc[post.reportedAt] = (acc[post.reportedAt] || 0) + 1;
      return acc;
    }, {});
  
    // Prepare data for the line chart
    const sortedDates = Object.keys(reportsByDate).sort();
    const reportCountsByDate = sortedDates.map(date => reportsByDate[date]);
  
    // Aggregate reports by location
    const reportsByLocation = posts.reduce((acc, post) => {
      acc[post.country] = (acc[post.country] || 0) + 1;
      return acc;
    }, {});
  
    const sortedLocations = Object.entries(reportsByLocation).sort((a, b) => b[1] - a[1]);
    const locations = sortedLocations.map(([country]) => country);
    const reportCounts = sortedLocations.map(([, count]) => count);
  
    // Calculate statistics
    const totalReports = posts.length;
    const openReports = posts.filter(post => post.status !== 'Resolved').length;
    const resolvedReports = posts.filter(post => post.status === 'Resolved').length;
  
    const openRateChange = 5.2;  // Example rate change
    const resolvedRateChange = -3.5;
  
    onMount(() => {
      // Reports by Location Bar Chart
      const ctxLocation = document.getElementById('reportsByLocation').getContext('2d');
      charts.reportsByLocation = new Chart(ctxLocation, {
        type: 'bar',
        data: {
          labels: locations,
          datasets: [{
            label: 'Reports by Location',
            data: reportCounts,
            backgroundColor: 'rgba(75, 192, 192, 0.6)',
            borderColor: 'rgba(75, 192, 192, 1)',
            borderWidth: 1,
          }],
        },
        options: { responsive: true },
      });
  
      // Reports Over Time Line Chart
      const ctxTime = document.getElementById('reportsOverTime').getContext('2d');
      charts.reportsOverTime = new Chart(ctxTime, {
        type: 'line',
        data: {
          labels: sortedDates,
          datasets: [{
            label: 'Number of Reports Over Time',
            data: reportCountsByDate,
            fill: false,
            borderColor: 'rgba(54, 162, 235, 1)',
            tension: 0.1,
          }],
        },
        options: { responsive: true },
      });
    });
  </script>
  
  <!-- Module Layout for Disaster Tracking Stats -->
  <div class="p-6 bg-gray-50">
    <h3 class="text-base font-semibold leading-6 text-gray-900">Last 30 days</h3>
    <dl class="mt-5 grid grid-cols-1 divide-y divide-gray-200 overflow-hidden rounded-lg bg-white shadow md:grid-cols-3 md:divide-x md:divide-y-0">
  
      <!-- Total Reports -->
      <div class="px-4 py-5 sm:p-6">
        <dt class="text-base font-normal text-gray-900">Total Reports</dt>
        <dd class="mt-1 text-2xl font-semibold text-indigo-600">{totalReports}</dd>
      </div>
  
      <!-- Open Reports -->
      <div class="px-4 py-5 sm:p-6">
        <dt class="text-base font-normal text-gray-900">Open Reports</dt>
        <dd class="mt-1 flex items-baseline text-2xl font-semibold text-indigo-600">
          {openReports}
          <span class="ml-2 text-sm font-medium text-gray-500">active cases</span>
        </dd>
      </div>
  
      <!-- Resolved Reports -->
      <div class="px-4 py-5 sm:p-6">
        <dt class="text-base font-normal text-gray-900">Resolved Reports</dt>
        <dd class="mt-1 flex items-baseline text-2xl font-semibold text-indigo-600">
          {resolvedReports}
          <span class="ml-2 text-sm font-medium text-gray-500">resolved cases</span>
        </dd>
      </div>
    </dl>
  </div>
  
    <!-- Reports by Location Bar Chart -->
    <div class="bg-white shadow rounded-lg p-4 mb-3">
      <h4 class="text-lg font-semibold text-gray-800 mb-2">Reports by Location</h4>
      <canvas id="reportsByLocation" class="w-full h-64"></canvas>
    </div>
    
    <!-- Reports Over Time Line Chart -->
    <div class="bg-white shadow rounded-lg p-4 mb-5">
        <h4 class="text-lg font-semibold text-gray-800 mb-2">Reports Over Time</h4>
        <canvas id="reportsOverTime" class="w-full h-64"></canvas>
    </div>
  