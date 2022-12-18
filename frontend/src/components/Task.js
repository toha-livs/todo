import { Link } from "react-router-dom";
import axiosBaseURL from '../httpCommon';

function Task (props){
    const deleteTask = () => {
        let taskId = props.task.id
        axiosBaseURL.delete(`/tasks/${taskId}/`)
        .then(res => {
            let tasks = props.tasks
            props.setTasks(tasks.filter(task => {return task.id !== taskId}));
        }).catch(err => {
            console.log(err)
        })
  }
    return (
        <tr className="text-center">
        <td className="text-start">{props.task.name}</td>
        <td><Link to={`/${props.task.id}`} className="btn border">Открыть {props.task.id}</Link></td>
        <td><button onClick={deleteTask} className="btn border">Удалить</button></td>
        </tr>
    )
}
export default  Task