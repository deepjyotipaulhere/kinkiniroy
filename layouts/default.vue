<template>
  <div>
    <div class="shadow">
      <div class="text-center" style="margin: 1em;margin-bottom:0"><img src="/img/kinkini.jpg" width="200px" height="auto"></div>
      <nav class="navbar navbar-light navbar-expand-md">
          <div class="d-flex w-50 order-2 justify-content-center">
              <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#collapsingNavbar">
                  <span class="navbar-toggler-icon"></span>
              </button>
          </div>
          <div class="navbar-collapse collapse justify-content-center order-2" id="collapsingNavbar">
              <ul class="navbar-nav">
                  <li class="nav-item p-2">
                      <a class="nav-link" href="#">Home <span class="sr-only">Home</span></a>
                  </li>
                  <li class="nav-item p-2">
                      <a class="nav-link" href="#">About</a>
                  </li>
                  <li class="nav-item p-2">
                      <a class="nav-link" href="#">Quillings</a>
                  </li>
                  <li class="nav-item p-2">
                      <a class="nav-link" href="#">Earrings</a>
                  </li>
                  <li class="nav-item p-2">
                      <a class="nav-link" href="#">Embroideries</a>
                  </li>
                  <li class="nav-item p-2">
                      <a class="nav-link" href="#">Contact</a>
                  </li>
              </ul>
          </div>
          <span class="navbar-text small text-truncate mt-1 w-50 text-right order-1 order-md-last"></span>
      </nav>
    </div>
    <nuxt />
  </div>
</template>

<style>
</style>
