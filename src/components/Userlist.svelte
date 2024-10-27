<script>
  export let posts = [];
  export let selectedPost = '';

  // Filter posts based on the selected post or nearby matches
  $: filteredPosts = selectedPost
    ? posts.filter((post) => post.title === selectedPost || isNearby(post))
    : posts;

  function isNearby(post) {
    return post.title.toLowerCase().includes(selectedPost.toLowerCase());
  }

  // Helper to generate slugs from post titles
  function toSlug(title) {
    return title
      .toLowerCase()
      .replace(/\s+/g, '-')
      .replace(/[^\w-]+/g, '');
  }
</script>

<!-- List of Posts with Image taking up 1/3 of the item -->
<ul role="list" class="divide-y divide-gray-100 bg-white shadow ring-1 ring-gray-900/5 sm:rounded-lg">
  {#each filteredPosts as post (post.title)}
    <li class="flex items-stretch gap-4 p-4 hover:bg-gray-50">
      <!-- Post Image (1/3 width) -->
      <a href={`/posts/${toSlug(post.title)}`} class="w-1/3">
        <img 
          class="w-full h-full object-cover rounded-md" 
          src={post.postImage} 
          alt={post.title} 
        />
      </a>

      <!-- Post Content (2/3 width) -->
      <a href={`/posts/${toSlug(post.title)}`} class="w-2/3 flex flex-col justify-between">
        <div class="space-y-2">
          <h3 class="text-lg font-semibold text-gray-900">{post.title}</h3>
          <p class="text-sm text-gray-500 line-clamp-3">{post.content}</p>
        </div>
        <div class="flex items-center gap-2 mt-4">
          <img 
            class="h-8 w-8 rounded-full object-cover" 
            src={post.profileImage} 
            alt={post.name} 
          />
          <p class="text-xs text-gray-400">{post.name} • {post.location}</p>
        </div>
      </a>
    </li>
  {/each}
</ul>
