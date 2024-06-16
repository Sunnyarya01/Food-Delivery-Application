<template>
  <div>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <div class="container">
        <a class="navbar-brand" href="/">FoodDelivery</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav"
          aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav ms-auto">
            <li class="nav-item">
              <a class="nav-link" href="#">Register as a Restaurant</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">Apply for Delivery Boy</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="/login">Login</a>
            </li>
            <li class="nav-item">
              <a class="btn btn-outline-primary" href="/signup">Sign Up</a>
            </li>
          </ul>
        </div>
      </div>
    </nav>

    <section class="hero-section text-center py-5">
      <div class="container">
        <h1 class="display-4">Order Your Favorite Food Anytime, Anywhere</h1>
        <p class="lead text-white">
          Discover the best food from over 1,000 restaurants and fast delivery to your doorstep.
        </p>
        <form action="#" class="mt-4">
          <div class="row justify-content-center">
            <div class="col-md-4 mb-3 mb-md-0">
              <select class="form-select" aria-label="Select Location">
                <option selected>Select Location</option>
                <option value="bengaluru">Bengaluru</option>
                <option value="chennai">Chennai</option>
              </select>
            </div>
            <div class="col-md-5 mb-3 mb-md-0">
              <div class="input-group">
                <input type="text" class="form-control" placeholder="Search for restaurants, dishes, or cuisine"
                  aria-label="Search" aria-describedby="search-button">
                <button class="btn btn-primary" type="button" id="search-button">Search</button>
              </div>
            </div>
          </div>
        </form>
      </div>
    </section>

    <section class="features-section py-5">
      <div class="container">
        <div class="row">
          <div class="col-md-4">
            <div class="feature-card text-center shadow-sm rounded overflow-hidden">
              <div class="card-img-top">
                <img src="../assets/foodverity.png" alt="Feature 1" class="img-fluid">
              </div>
              <div class="card-body">
                <h4 class="card-title m-3">Wide Variety</h4>
                <p class="card-text m-3 text-left">
                  Choose from a wide range of cuisines and dishes. Discover new flavors and enjoy the best food experience.
                </p>
              </div>
            </div>
          </div>
          <div class="col-md-4">
            <div class="feature-card text-center shadow-sm rounded overflow-hidden">
              <div class="card-img-top">
                <img src="../assets/delivery.png" alt="Feature 2" class="img-fluid">
              </div>
              <div class="card-body">
                <h4 class="card-title m-3">Fast Delivery</h4>
                <p class="card-text m-3 text-left">
                  Get your food delivered to your doorstep quickly. Enjoy hassle-free delivery service with guaranteed satisfaction.
                </p>
              </div>
            </div>
          </div>
          <div class="col-md-4">
            <div class="feature-card text-center shadow-sm rounded overflow-hidden">
              <div class="card-img-top">
                <img src="../assets/payment.png" alt="Feature 3" class="img-fluid">
              </div>
              <div class="card-body">
                <h4 class="card-title m-3">Easy Payment</h4>
                <p class="card-text m-3 text-left">
                  Convenient payment options including credit card, debit card, and more. Secure transactions for peace of mind.
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: "LandingPage",
};
</script>

<style>
.hero-section {
  background: url('https://b.zmtcdn.com/web_assets/81f3ff974d82520780078ba1cfbd453a1583259680.png') no-repeat center center;
  background-size: cover;
  color: white;
}

.navbar-light .navbar-nav .nav-link {
  color: #333;
  font-weight: 500;
}

.navbar-light .navbar-brand {
  color: #0d6efd;
  font-size: 1.5rem;
  font-weight: bold;
}

.hero-section .display-4 {
  color: #fff;
  font-weight: bold;
}

.features-section {
  background-color: #f8f9fa;
}

.features-section .feature-card {
  background-color: #fff;
  transition: transform 0.3s ease-in-out;
  height: 100%;
}

.features-section .feature-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.features-section .card-img-top {
  overflow: hidden;
}

.features-section .card-img-top img {
  width: 100%;
  height: auto;
  transition: transform 0.3s ease-in-out;
}

.features-section .feature-card:hover .card-img-top img {
  transform: scale(1.1);
}

.features-section h4 {
  color: #333;
}

.features-section p {
  color: #555;
  text-align: left;
}
</style>
