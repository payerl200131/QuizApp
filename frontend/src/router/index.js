import { createRouter, createWebHistory } from 'vue-router'
import QuizzesView from '../views/QuizzesView.vue'
import ProfileView from '../views/ProfileView.vue'
import LoginView from '../views/LoginView.vue'
import RegisterView from '../views/RegisterView.vue'
import LogoutView from '../views/LogoutView.vue'
import RefreshView from '../views/RefreshView.vue'
import QuizPlayView from '../views/QuizPlayView.vue'
import QuizAddView from '../views/QuizAddView.vue'
import QuizUpdateView from '../views/QuizUpdateView.vue'
import { useAuthStore } from '../store/auth'
import UserView from '../views/UserView.vue'

const routes = [
    {
        path: '/',
        name: 'Home',
        component: QuizzesView,
    },
    {
        path: '/play/:id',
        name: 'Play',
        component: QuizPlayView,
        meta: { requiresAuth: true },
    },
    {
        path: '/update/:id',
        name: 'QuizUpdate',
        component: QuizUpdateView,
        meta: { requiresAuth: true },
    },
    {
        path: '/create/',
        name: 'Add',
        component: QuizAddView,
        meta: { requiresAuth: true },
    },
    {
        path: '/register',
        name: 'Register',
        component: RegisterView,
    },
    {
        path: '/login',
        name: 'Login',
        component: LoginView,
    },
    {
        path: '/profile',
        name: 'Profile',
        component: ProfileView,
        meta: { requiresAuth: true },
    },
    {
        path: '/logout',
        name: 'Logout',
        component: LogoutView,
    },
    {
        path: '/refresh',
        name: 'Refresh',
        component: RefreshView,
    },
    {
        path: '/users',
        name: 'User',
        component: UserView,
    },
]

const router = createRouter({
    history: createWebHistory(),
    routes, // short for `routes: routes`
})

router.beforeEach((to, from , next) => {
    const auth = useAuthStore();
    if (to.matched.some((record) => record.meta.requiresAuth)) {
        if (auth.isAuthenticated) {
            next();
            return;
        }
        next("/login");
    } else {
        next();
    }

})

export default router;