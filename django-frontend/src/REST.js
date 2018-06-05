import React from 'react';
import Note from './Note';

import axios from 'axios';

class REST extends React.Component {
  state = {
    notes: []
  }

  componentWillMount() {
    axios
      .get(
        'http://localhost:8000/api/notes/',
        { headers: { "Authorization": `Token 2051ee8bf249949fc6a72c9f35e49f0d5699101c` }}
      )
      .then(res => {
        console.log(res.data);
        this.setState({ notes: res.data });
      })
      .catch(err => {
        console.error(err);
      });
  }

  render() {
    return (
      <div>
        {this.state.notes.map(note => <Note key={note.id} note={note} /> )}
      </div>
    )
  }
}

export default REST;