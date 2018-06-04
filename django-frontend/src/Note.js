import React from 'react';

class Note extends React.Component {
  render () {
    return (
      <div>
        <div>
          {this.props.note.title} {this.props.note.content}
        </div>
      </div>
    )
  }

  _voteForNote = async () => {

  };
}

export default Note;
