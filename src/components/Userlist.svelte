<script>
  export let posts = [];
  export let selectedPost = '';

  $: filteredPosts = selectedPost
    ? posts.filter((post) => post.title === selectedPost || isNearby(post))
    : [...posts];

  function isNearby(post) {
    return post.title.toLowerCase().includes(selectedPost.toLowerCase());
  }

  // Helper to convert titles into URL-friendly slugs
  function toSlug(title) {
  return title
    .toLowerCase()
    .replace(/\s+/g, '-') // Replace spaces with hyphens
    .replace(/[^\w-]+/g, ''); // Remove non-word characters
}

</script>

<ul
  role="list"
  class="divide-y divide-gray-100 overflow-hidden bg-white shadow-sm ring-1 ring-gray-900/5 sm:rounded-lg"
>
  {#each filteredPosts as post (post.title)}
    <li class="relative flex gap-x-4 px-3 py-4 hover:bg-gray-50 sm:px-5">
      <a href={`/posts/${toSlug(post.title)}`} class="w-full" on:click={(e) => handleLinkClick(e, post)}>
        <div class="flex gap-x-3 items-center">
          <img
            class="h-10 w-10 rounded-full object-cover"
            src={post.profileImage}
            alt={post.name}
          />
          <div class="flex-1 min-w-0">
            <p class="text-sm font-semibold leading-5 text-gray-900 truncate">
              {post.title}
            </p>
            <p class="mt-0.5 text-sm text-gray-500 leading-relaxed">
              {post.content}
            </p>
            <p class="text-xs text-gray-400">{post.name}</p>
          </div>
        </div>

        <img
          class="mt-2 w-full h-40 sm:h-56 object-cover rounded-md"
          src={post.postImage}
          alt={post.title}
        />
      </a>
    </li>
  {/each}
</ul>
