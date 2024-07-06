/* eslint-disable no-unused-vars */
import React from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import Header from './Header';
import Navigation from './Navigation';
import TrendingPage from './TrendingPage';
import NewsPage from './NewsPage';
import CategoriesPage from './CategoriesPage';
import LoginPage from './LoginPage';
import RegisterPage from './RegisterPage';
import ShowList from './ShowList';
import ShowDetails from './ShowDetails';
import ShowForm from './ShowForm';

function App() {
  return (
    <BrowserRouter>
      <Header />
      <Navigation />
      <Switch>
        <Route path="/" exact component={TrendingPage} />
        <Route path="/news" component={NewsPage} />
        <Route path="/categories" component={CategoriesPage} />
        <Route path="/login" component={LoginPage} />
        <Route path="/register" component={RegisterPage} />
        <Route path="/shows" exact component={ShowList} />
        <Route path="/shows/:id" component={ShowDetails} />
        <Route path="/shows/create" component={ShowForm} />
      </Switch>
    </BrowserRouter>
  );
}

export default App;