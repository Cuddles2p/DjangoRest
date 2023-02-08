import React from "react"


const BookItem =({item}) => {
    return (
        <tr>
            <td>
                {item.id}
            </td>
            <td>
                {item.name}
            </td>
            <td>
                {item.author}
            </td>
        </tr>
    )
}


const BookList = ({items}) => {
    return (
        <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Name</th>
                    <th>Author</th>
                </tr>
            </thead>
            {items.map((item) => <BookItem item={item} />)}
        </table>
    )
}


export default BookList