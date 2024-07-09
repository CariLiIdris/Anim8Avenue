/* eslint-disable no-unused-vars */
import React from 'react';
import { Route, Routes } from 'react-router-dom';
import Header from './components/Header.jsx';
import Navigation from "./components/Navigation.jsx"
import TrendingPage from './components/TrendingPage.jsx';
import NewsPage from './components/NewsPage.jsx';
import CategoriesPage from './components/CategoriesPage.jsx';
import LoginPage from './components/LoginPage.jsx';
import RegisterPage from './components/RegisterPage.jsx';
import ShowList from './components/ShowList.jsx';
import ShowDetails from './components/ShowDetails.jsx';
import ShowForm from './components/ShowForm.jsx';
import ProfilePage from './components/ProfilePage.jsx';
import { logout } from './services/userService.jsx';

function App() {
  return (
    <>
      <Header />
      <Navigation submitFunction={logout} />
      <Routes>
        <Route
          path="/"
          exact
          element={<TrendingPage />}
        />

        <Route path="/news" element={<NewsPage />}
        />

        <Route
          path="/categories"
          element={<CategoriesPage />}
        />

        <Route
          path="/login"
          element={<LoginPage />}
        />

        <Route
          path="/profile"
          element={<ProfilePage />}
        />

        <Route
          path="/register"
          element={<RegisterPage />}
        />

        <Route
          path="/shows"
          exact
          element={<ShowList />}
        />

        <Route
          path="/shows/:id"
          element={<ShowDetails />}
        />

        <Route
          path="/shows/create"
          element={<ShowForm />}
        />

      </Routes>
    </>
  );
}

export default App;