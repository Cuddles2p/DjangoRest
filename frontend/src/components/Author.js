import React from "react"


const AuthorItem =({auhtor}) => {
    return (
        <tr>
            <td>
                {auhtor.first_name}
            </td>
            <td>
                {auhtor.last_name}
            </td>
            <td>
                {auhtor.birthday_year}
            </td>
        </tr>
    )
}

const AuthorList = ({authors}) => {
    return (
        <table>
            <th>
                First name
            </th>
            <th>
                Last name
            </th>
            <th>
                Birthday year
            </th>
            {authors.map((author) => <AuthorItem auhtor={author} />)}
        </table>
    )
}


export default AuthorList