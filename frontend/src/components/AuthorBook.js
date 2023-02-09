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


const AuthorBookList = ({items}) => {
    let {id} = useParams()
    let filtered_items = items.filter((item) => item.author.id === id)
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
            {filtered_items.map((item) => <BookItem item={item} />)}
        </table>
    )
}


export default AuthorBookList