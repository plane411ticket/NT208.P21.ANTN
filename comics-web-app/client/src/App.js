import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import HomePage from './pages/HomePage';
import ComicPage from './pages/ComicPage';
import AudioComicPage from './pages/AudioComicPage';
import StoryPage from './pages/StoryPage';

function App() {
  return (
    <Router>
      <div>
        <Switch>
          <Route path="/" exact component={HomePage} />
          <Route path="/comics/:id" component={ComicPage} />
          <Route path="/audio-comics/:id" component={AudioComicPage} />
          <Route path="/stories/:id" component={StoryPage} />
        </Switch>
      </div>
    </Router>
  );
}

export default App;