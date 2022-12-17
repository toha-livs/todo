import Task from './Task'

function TaskList (props){
    console.log(props.tasks)
    return (<table className="table table-bordered">
        <tbody>
            <tr className="text-center">
                <th>Задания</th>
                <th>Просмотр на новой странице</th>
                <th>Удаление</th>
            </tr>
            {props.tasks.length > 0 &&
                props.tasks.map(task => <Task task={task} />)
            }
        </tbody>

    </table>)
}
export default  TaskList