<script>
    import { onMount } from 'svelte';
    import Chart from 'chart.js/auto';
  
    let charts = {}; // Store chart instances
  
    // Example user data
    const userData = [
      { name: 'John Doe', location: 'New York, NY, USA', reports: 5, status: 'open' },
      { name: 'Jane Smith', location: 'San Bernardino, CA, USA', reports: 12, status: 'resolved' },
      { name: 'Emily Johnson', location: 'Lake Charles, LA, USA', reports: 3, status: 'open' },
      { name: 'Hideo Takahashi', location: 'Tokyo, Japan', reports: 8, status: 'open' },
      { name: 'Yuki Tanaka', location: 'Kyushu, Japan', reports: 4, status: 'resolved' },
      { name: 'Ravi Kumar', location: 'Himachal Pradesh, India', reports: 10, status: 'open' },
      { name: 'Carlos Martinez', location: 'Seville, Spain', reports: 2, status: 'resolved' },
      { name: 'Alyssa Reyes', location: 'Manila, Philippines', reports: 15, status: 'resolved' }
    ];
  
    // Calculate total reports, open reports, and resolved reports
    const totalReports = userData.reduce((sum, user) => sum + user.reports, 0);
    const openReports = userData.filter(user => user.status === 'open').reduce((sum, user) => sum + user.reports, 0);
    const resolvedReports = userData.filter(user => user.status === 'resolved').reduce((sum, user) => sum + user.reports, 0);
  
    // Example rate changes (you could also calculate these dynamically if needed)
    const openRateChange = 5.2;  // Increase by 5.2%
    const resolvedRateChange = -3.5;  // Decrease by 3.5%
  
    // Sort data by number of reports
    const sortedData = [...userData].sort((a, b) => b.reports - a.reports);
  
    onMount(() => {
      const ctx = document.getElementById('reportsByLocation').getContext('2d');
      charts.reportsByLocation = new Chart(ctx, {
        type: 'bar',
        data: {
          labels: sortedData.map(user => user.location),
          datasets: [{
            label: 'Reports by Location',
            data: sortedData.map(user => user.reports),
            backgroundColor: 'rgba(75, 192, 192, 0.6)',
            borderColor: 'rgba(75, 192, 192, 1)',
            borderWidth: 1
          }]
        },
        options: { responsive: true }
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
        <dd class="mt-1 flex items-baseline justify-between md:block lg:flex">
          <div class="flex items-baseline text-2xl font-semibold text-indigo-600">
            {totalReports}
          </div>
        </dd>
      </div>
  
      <!-- Open Reports -->
      <div class="px-4 py-5 sm:p-6">
        <dt class="text-base font-normal text-gray-900">Open Reports</dt>
        <dd class="mt-1 flex items-baseline justify-between md:block lg:flex">
          <div class="flex items-baseline text-2xl font-semibold text-indigo-600">
            {openReports}
            <span class="ml-2 text-sm font-medium text-gray-500">active cases</span>
          </div>
          <div
            class={`inline-flex items-baseline rounded-full px-2.5 py-0.5 text-sm font-medium 
            ${openRateChange >= 0 ? 'bg-green-100 text-green-800' : 'bg-red-100 text-red-800'}`}
          >
            <svg
              class={`-ml-1 mr-0.5 h-5 w-5 ${
                openRateChange >= 0 ? 'text-green-500' : 'text-red-500'
              }`}
              viewBox="0 0 20 20" fill="currentColor" aria-hidden="true"
            >
              <path
                fill-rule="evenodd"
                d="M10 17a.75.75 0 0 1-.75-.75V5.612L5.29 9.77a.75.75 0 0 1-1.08-1.04l5.25-5.5a.75.75 0 1 1-1.08 1.04l-3.96-4.158V16.25A.75.75 0 0 1 10 17Z"
                clip-rule="evenodd"
              />
            </svg>
            {Math.abs(openRateChange)}%
          </div>
        </dd>
      </div>
  
      <!-- Resolved Reports -->
      <div class="px-4 py-5 sm:p-6">
        <dt class="text-base font-normal text-gray-900">Resolved Reports</dt>
        <dd class="mt-1 flex items-baseline justify-between md:block lg:flex">
          <div class="flex items-baseline text-2xl font-semibold text-indigo-600">
            {resolvedReports}
            <span class="ml-2 text-sm font-medium text-gray-500">resolved cases</span>
          </div>
          <div
            class={`inline-flex items-baseline rounded-full px-2.5 py-0.5 text-sm font-medium 
            ${resolvedRateChange >= 0 ? 'bg-green-100 text-green-800' : 'bg-red-100 text-red-800'}`}
          >
            <svg
              class={`-ml-1 mr-0.5 h-5 w-5 ${
                resolvedRateChange >= 0 ? 'text-green-500' : 'text-red-500'
              }`}
              viewBox="0 0 20 20" fill="currentColor" aria-hidden="true"
            >
              <path
                fill-rule="evenodd"
                d="M10 3a.75.75 0 0 1 .75.75v10.638l3.96-4.158a.75.75 0 1 1 1.08 1.04l-5.25 5.5a.75.75 0 0 1-1.08 0l-5.25-5.5a.75.75 0 1 1 1.08-1.04l3.96 4.158V3.75A.75.75 0 0 1 10 3Z"
                clip-rule="evenodd"
              />
            </svg>
            {Math.abs(resolvedRateChange)}%
          </div>
        </dd>
      </div>
    </dl>
  </div>
  
  <!-- Sorted Bar Chart -->
  <div class="p-6 bg-gray-50">
    <canvas id="reportsByLocation" class="w-full h-64"></canvas>
  </div>
  