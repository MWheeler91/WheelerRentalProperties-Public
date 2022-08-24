import { createRouter, createWebHistory } from 'vue-router';
import HomePage from '../components/Pages/HomePage'
import propertyPage from "@/components/Pages/PropertyPage";
import applicationPage from "@/components/Pages/ApplicationPage";
import contactPage from "@/components/Pages/ContactPage";
import registrationPage from "@/components/Pages/Registration/RegistrationPage";
import loginPage from "@/components/Pages/Registration/LoginPage";
import PasswordReset from "@/components/Pages/Registration/PasswordReset";
import store from '../store'
import propertyDetails from "@/components/Properties/PropertyDetails";


const index = createRouter({
  scrollBehavior(to, from, savedPosition) {
    console.log(to, from, savedPosition)
    return { top: 0 }
  },
  history: createWebHistory(),

  routes: [
    {
      path: '/',
      name: 'Home',
      component: HomePage,
    },
    {
      path: '/properties',
      name: 'Properties',
      component: propertyPage,
    },
    {
      path: '/properties/:slug/',
      name: 'propertyDetails',
      component: propertyDetails,
      props: true
    },
    {
      path: '/application/id=:id?/address=:address?',
      // path: '/application/',
      name: 'Application',
      component: applicationPage,
      meta: {
        requireLogin: true
      }
    },
    {
      path: '/contact',
      name: 'Contact',
      component: contactPage,
    },
    {
      path: '/login',
      name: 'Login',
      component: loginPage
    },
    {
      path: '/registration',
      name: 'Registration',
      component: registrationPage
    },
    {
      path: '/password_reset',
      name: 'PasswordReset',
      component: PasswordReset
    },
  ],
  linkActiveClass: 'active',


})

index.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
    next('/login')
  } else{
    next()
  }
})

export function resetRouter() {
  const newRouter = createRouter()
  index.matcher = newRouter.matcher // reset index
}

export default index