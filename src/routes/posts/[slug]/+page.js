// src/routes/posts/[slug]/+page.js
export async function load({ params }) {
  console.log('Received slug:', params.slug); // Ensure the slug is received

  const posts = [
    {
      title: 'Severe Flooding in New York City',
      slug: 'severe-flooding-in-new-york-city',
      content:
        'Unprecedented flooding in Lower Manhattan has led to the evacuation of several neighborhoods. The subway system is halted, and rescue operations are underway. Please avoid the area and call 311 for non-emergency inquiries.',
      postImage: '/banner4.jpg',
      profileImage: '/pfp1.jpg',
      name: 'John Doe',
      location: 'New York, NY, USA',
      category: 'Flooding',
      reportedTime: '2 hours ago',
      status: 'Ongoing',
      emergencyContacts: ['311', 'NYC OEM'],
    },
    {
      title: 'California Wildfire Spreading Rapidly',
      slug: 'california-wildfire-spreading-rapidly',
      content:
        'A wildfire near San Bernardino has grown to over 10,000 acres. Evacuation orders are in effect for surrounding areas. Air quality is poor across the region, and residents are urged to stay indoors.',
      postImage: '/banner1',
      profileImage: '/pfp2.jpg',
      name: 'Jane Smith',
      location: 'San Bernardino, CA, USA',
      category: 'Wildfire',
      reportedTime: '1 hour ago',
      status: 'Evacuations Ongoing',
      emergencyContacts: ['911', 'Cal Fire'],
    },
    {
      title: 'Hurricane Laura Makes Landfall',
      slug: 'hurricane-laura-makes-landfall',
      content:
        'Hurricane Laura has hit Louisiana as a Category 4 storm, with winds exceeding 150 mph. Power outages have been reported in Lake Charles and nearby cities. Stay sheltered and avoid all unnecessary travel.',
      postImage: '/banner4',
      profileImage: '/pfp3.jpg',
      name: 'Emily Johnson',
      location: 'Lake Charles, LA, USA',
      category: 'Hurricane',
      reportedTime: '3 hours ago',
      status: 'Critical',
      emergencyContacts: ['911', 'FEMA'],
    },
    {
      title: 'Earthquake Hits Southern Japan',
      slug: 'earthquake-hits-southern-japan',
      content:
        'A magnitude 6.8 earthquake shook the southern islands of Japan. Aftershocks continue to be felt in the region, and tsunami warnings have been issued. No major casualties reported yet, but infrastructure damage is significant.',
      postImage: '/banner3.jpg',
      profileImage: '/pfp4.jpg',
      name: 'Hideo Takahashi',
      location: 'Kyushu, Japan',
      category: 'Earthquake',
      reportedTime: '30 minutes ago',
      status: 'Monitoring Aftershocks',
      emergencyContacts: ['119', 'Japan Meteorological Agency'],
    },
    {
      title: 'Tornado in Oklahoma Destroys Homes',
      slug: 'tornado-in-oklahoma-destroys-homes',
      content:
        'A large tornado has touched down in Moore, Oklahoma, destroying several homes and vehicles. Emergency responders are on the scene, and residents are being advised to take shelter immediately.',
      postImage: '/banner4.jpg',
      profileImage: '/pfp3.jpg',
      name: 'Mike Andrews',
      location: 'Moore, OK, USA',
      category: 'Tornado',
      reportedTime: '45 minutes ago',
      status: 'First Responders on Site',
      emergencyContacts: ['911', 'American Red Cross'],
    },
    {
      title: 'Massive Landslide in Northern India',
      slug: 'massive-landslide-in-northern-india',
      content:
        'A major landslide in the Himalayan region has blocked roads and caused multiple injuries. Rescue teams are struggling to reach remote villages affected by the landslide. Helicopters have been deployed for rescue.',
      postImage: '/banner3.jpg',
      profileImage: '/pfp2.jpg',
      name: 'Ravi Kumar',
      location: 'Himachal Pradesh, India',
      category: 'Landslide',
      reportedTime: '1 hour ago',
      status: 'Rescue Operations Underway',
      emergencyContacts: ['108', 'Disaster Management Authority'],
    },
    {
      title: 'Heatwave in Spain Leads to Health Alerts',
      slug: 'heatwave-in-spain-leads-to-health-alerts',
      content:
        'Spain is experiencing an extreme heatwave, with temperatures exceeding 45°C (113°F). Health authorities have issued alerts, urging residents to stay hydrated and avoid outdoor activities during peak hours.',
      postImage: '/banner2.jpg',
      profileImage: '/pfp1.jpg',
      name: 'Carlos Martinez',
      location: 'Seville, Spain',
      category: 'Heatwave',
      reportedTime: '2 days ago',
      status: 'Health Alert Issued',
      emergencyContacts: ['112', 'Spanish Red Cross'],
    },
    {
      title: 'Flash Floods in the Philippines',
      slug: 'flash-floods-in-the-philippines',
      content:
        'Heavy rainfall has caused flash floods across Manila, submerging roads and disrupting transportation. Evacuation centers are being set up, and residents are advised to move to higher ground.',
      postImage: '/banner1.jpg',
      profileImage: '/pfp2.jpg',
      name: 'Alyssa Reyes',
      location: 'Manila, Philippines',
      category: 'Flash Flood',
      reportedTime: '4 hours ago',
      status: 'Evacuations in Progress',
      emergencyContacts: ['911', 'Philippine Red Cross'],
    }
  ];
  

  // Find the post matching the slug
  const post = posts.find((p) => p.slug === params.slug);
  console.log('Found post:', post); // Ensure the post is found

  if (!post) {
    return {
      status: 404,
      error: new Error('Post not found'),
    };
  }

  // Pass the post data to the page component
  return { post };
}
