<script>
  const navItems = [
    { name: "Home", href: "/" },
    { name: "Blog", href: "/blog" },
    { name: "Archive", href: "/archive" },
    { name: "Photos", href: "/photos" },
    { name: "Bookshelf", href: "/bookshelf" },
    { name: "Gear", href: "/gear" },
    { name: "Newsletter", href: "/newsletter" }
  ];

  let menuOpen = false;
</script>

<style>
  nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1rem 2rem;
    /* font-family: "Helvetica Neue", Helvetica, Arial, sans-serif; */
    font-weight: 300;
    background-color: #fff;
    border-bottom: 1px solid #eaeaea;
    position: relative;
  }

  .brand {
    font-weight: 500;
    font-size: 1.25rem;
    letter-spacing: 0.05em;
  }

  .nav-links {
    display: flex;
    gap: 2rem;
  }

  .nav-links a {
    text-decoration: none;
    color: #111;
    font-weight: 300;
    transition: color 0.2s ease;
  }

  .nav-links a:hover {
    color: #0070f3;
  }

  .mobile-menu-button {
    display: none;
    font-size: 1.5rem;
    background: none;
    border: none;
    cursor: pointer;
  }

  @media (max-width: 768px) {
    .nav-links {
      display: none;
      flex-direction: column;
      gap: 1rem;
      position: absolute;
      top: 100%;
      left: 0;
      right: 0;
      background-color: #fff;
      padding: 1rem 2rem;
      border-bottom: 1px solid #eaeaea;
    }

    .nav-links.open {
      display: flex;
    }

    .mobile-menu-button {
      display: block;
    }
  }
</style>

<nav>
  <div class="brand">ZMH</div>

  <button class="mobile-menu-button" on:click={() => menuOpen = !menuOpen}>
    ☰
  </button>

  <div class="nav-links" class:open={menuOpen}>
    {#each navItems as item}
      <a href={item.href}>{item.name}</a>
    {/each}
  </div>
</nav>
