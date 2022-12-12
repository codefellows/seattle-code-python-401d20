import React from 'react';

// the reason we used props['thing-count'] syntax below

// obj.key is fine
// obj.key-with-hyphen not fine

// key = 'foo'
// obj[key] == 'foo' is true

export default props => (
    <>
        <h2>Header</h2>
        <p>{props['thing-count']}</p>
    </>
)
