<script>
  export let posts = []; // List of all posts
  export let selectedPost = ''; // Selected post title

  // Helper to generate slugs from post titles
  function toSlug(title) {
    return title
      .toLowerCase()
      .replace(/\s+/g, '-')
      .replace(/[^\w-]+/g, '');
  }

  // Separate the selected post from the rest
  $: [selected, rest] = posts.reduce(
    ([selected, rest], post) => {
      if (post.title === selectedPost) selected = post;
      else rest.push(post);
      return [selected, rest];
    },
    [null, []]
  );
</script>

<!-- List of Posts -->
<div class="bg-white shadow ring-1 ring-gray-900/5 sm:rounded-lg">
  <!-- Selected Post Section -->
  {#if selected}
    <div class="p-3">
      <h2 class="text-lg font-semibold text-gray-900 mb-2">{selected.location}</h2>
      <ul role="list">
        <li class="flex items-stretch gap-3 p-3 hover:bg-gray-50">
          <!-- Post Image (1/3 width) -->
          <a href={`/posts/${toSlug(selected.title)}`} class="w-1/3">
            <img 
              class="w-full h-full object-cover rounded-md" 
              src={selected.postImage} 
              alt={selected.title} 
            />
          </a>

          <!-- Post Content (2/3 width) -->
          <a href={`/posts/${toSlug(selected.title)}`} class="w-2/3 flex flex-col justify-between">
            <div class="space-y-1">
              <h3 class="text-md font-semibold text-gray-900">{selected.title}</h3>
              <p class="text-sm text-gray-500 line-clamp-3">{selected.content}</p>
            </div>
            <div class="flex items-center gap-2 mt-2">
              <img 
                class="h-6 w-6 rounded-full object-cover" 
                src={selected.profileImage} 
                alt={selected.name} 
              />
              <p class="text-xs text-gray-400">{selected.name} • {selected.location}</p>
            </div>
          </a>
        </li>
      </ul>
      <!-- Divider between sections -->
      <div class="border-t border-gray-200 mt-3"></div>
    </div>
  {/if}

  <!-- Rest of the Posts Section -->
  {#if rest.length > 0}
    <div class="p-3">
      {#if selected}
        <h2 class="text-lg font-semibold text-gray-900 mb-2">Other Posts</h2>
      {/if}
      <ul role="list" class="divide-y divide-gray-100">
        {#each rest as post (post.title)}
          <li class="flex items-stretch gap-3 p-3 hover:bg-gray-50">
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
              <div class="space-y-1">
                <h3 class="text-md font-semibold text-gray-900">{post.title}</h3>
                <p class="text-sm text-gray-500 line-clamp-3">{post.content}</p>
              </div>
              <div class="flex items-center gap-2 mt-2">
                <img 
                  class="h-6 w-6 rounded-full object-cover" 
                  src={post.profileImage} 
                  alt={post.name} 
                />
                <p class="text-xs text-gray-400">{post.name} • {post.location}</p>
              </div>
            </a>
          </li>
        {/each}
      </ul>
    </div>
  {/if}
</div>
