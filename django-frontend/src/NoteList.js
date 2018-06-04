import React from 'react';
import Note from './Note';

import { graphql } from 'react-apollo';
import gql from 'graphql-tag';

class NoteList extends React.Component {
  render() {
    console.log('props:', this.props);
    
    if (this.props.data && this.props.data.loading) {
      return <div>Loading</div>
    }

    if (this.props.data && this.props.data.error) {
      // console.log(Object.values(this.props.feedQuery.error));
      return <div>Error</div>
    }

    const notesToRender = this.props.data.notes

    return (
      <div>
        {notesToRender.map(note => <Note key={note.id} note={note} /> )}
      </div>
    )
  }
}

const FEED_QUERY = gql`
  query {
    notes {
      id
      title
      content
    }
  }
`;

console.log(FEED_QUERY);

export default graphql(FEED_QUERY) (NoteList);
