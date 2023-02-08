import React from "react"
import {useParams} from "react-router-dom"


const BookItem = ({item}) => {
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


const AuthorBookList = ({books}) => {
    let {id} = useParams()
    let filtered_books = books.filter((book) => book.author.id === id)
    return (
        <table>
            <thead>
                <tr>
                    <th>
                        ID
                    </th>
                    <th>
                        Name
                    </th>
                    <th>
                        Author
                    </th>
                </tr>
            </thead>
            {filtered_books.map((book) => <BookItem book={book} />)}
        </table>
    )
}


export default AuthorBookList