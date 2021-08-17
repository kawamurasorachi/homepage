export default {
  // Global page headers: https://go.nuxtjs.dev/config-head
  head: {
    title: "front",
    htmlAttrs: {
      lang: "en"
    },
    meta: [
      { charset: "utf-8" },
      { name: "viewport", content: "width=device-width, initial-scale=1" },
      { hid: "description", name: "description", content: "" },
      { name: "format-detection", content: "telephone=no" }
    ],
    link: [{ rel: "icon", type: "image/x-icon", href: "/favicon.ico" }]
  },

  server: {
    port: 3000,
    host: "0.0.0.0"
  },

  // Global CSS: https://go.nuxtjs.dev/config-css
  css: [{ src: "~/assets/main.scss", lang: "scss" }],

  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: [
    {
      src: "@/plugins/vue-mavon-editor",
      srr: false
    }
  ],

  // Auto import components: https://go.nuxtjs.dev/config-components
  components: true,

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: ["@nuxtjs/composition-api/module"],

  // Modules: https://go.nuxtjs.dev/config-modules
  modules: [
    // https://go.nuxtjs.dev/axios
    "@nuxtjs/axios",
    "@nuxtjs/auth-next",
    "@nuxtjs/style-resources"
  ],

  styleResources: {
    scss: ["~/assets/_variable.scss"]
  },

  // Axios module configuration: https://go.nuxtjs.dev/config-axios
  axios: {
    baseURL: "http://django:8001/api",
    browserBaseURL: "http://localhost/api"
  },

  auth: {
    redirect: {
      login: "/manage/login",
      home: "/manage",
      logout: "/"
    },
    strategies: {
      local: {
        token: {
          property: "auth_token",
          type: "Token"
        },
        user: {
          property: false
        },
        endpoints: {
          login: {
            url: "/auth/token/login/",
            method: "post"
          },
          logout: { url: "/auth/token/logout/", method: "post" },
          user: {
            url: "/auth/users/me/",
            method: "get"
          }
        }
      }
    }
  },

  // Build Configuration: https://go.nuxtjs.dev/config-build
  build: {}
};
