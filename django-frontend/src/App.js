import React from 'react';
import NoteList from './NoteList';
import REST from './REST';

class App extends React.Component {
  render() {
    return (
      <div>
        <NoteList />
        <hr/>
        <REST />
      </div>
    )
  }
}

export default App;
