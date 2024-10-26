export async function load({ params }) {
  console.log('Received slug:', params.slug); // Check if the slug is being passed

  const posts = [
    {
      title: 'Flooding in New York',
      slug: 'flooding-in-new-york',
      content: 'Severe flooding...',
      postImage: '/banner1.jpg',
      name: 'John Doe',
    },
  ];

  const post = posts.find((p) => p.slug === params.slug);

  console.log('Found post:', post); // Check if the post is found

  if (!post) {
    return {
      status: 404,
      error: new Error('Post not found'),
    };
  }

  return {
    props: { post },
  };
}

