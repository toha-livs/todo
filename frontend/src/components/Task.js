import { Link } from "react-router-dom";

function Task (props){
    return (
        <tr className="text-center">
        <td className="text-start">{props.task.name}</td>
        <td><Link to={`/${props.task.id}`} className="btn border">Открыть {props.task.id}</Link></td>
        <td><button className="btn border">Удалить</button></td>
        </tr>
    )
}
export default  Task