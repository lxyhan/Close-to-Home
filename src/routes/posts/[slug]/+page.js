// src/routes/posts/[slug]/+page.js
export async function load({ params }) {
  console.log('Received slug:', params.slug); // Ensure the slug is received

  let posts = [
    {
      title: 'Flooding in New York Traps Residents',
      slug: 'flooding-in-new-york-traps-residents',
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
      slug: 'earthquake-aftermath-in-turkey',
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
      slug: 'typhoon-haikui-wrecks-coastal-villages',
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
      slug: 'wildfire-evacuees-need-supplies',
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
      slug: 'tornado-in-texas-causes-power-outage',
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
      slug: 'hurricane-ian-floods-florida-towns',
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
      slug: 'flash-floods-in-malaysia-submerge-towns',
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
      slug: 'volcanic-eruption-in-indonesia',
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
      slug: 'blizzard-in-canada-traps-travelers',
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
      slug: 'monsoon-floods-worsen-in-bangladesh',
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
