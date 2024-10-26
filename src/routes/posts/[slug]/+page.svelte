<script>
  export let post; // Declare the prop to receive the post

  console.log('Received post:', post); // Check if it logs the post correctly
</script>

{#if post}
  <article class="p-6 max-w-3xl mx-auto bg-white shadow-md rounded-md">
    <h1 class="text-2xl font-bold mb-4">{post.title}</h1>
    <div class="flex items-center gap-4 mb-6">
      <img class="h-10 w-10 rounded-full" src={post.postImage} alt={post.name} />
      <p class="text-sm text-gray-600">By {post.name}</p>
    </div>
    <p class="text-gray-700">{post.content}</p>
  </article>
{:else}
  <p>Loading post...</p>
{/if}
