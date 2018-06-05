import React from 'react';

class Note extends React.Component {
  render () {
    return (
      <div>
        <div>
          {this.props.note.title} {this.props.note.content} {this.props.note.id}
        </div>
      </div>
    )
  }

  _voteForNote = async () => {

  };
}

export default Note;
