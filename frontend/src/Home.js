import { useState, useEffect } from 'react'
import Task from './components/Task'
import Alert from 'react-bootstrap/Alert'

import axios from 'axios';


function Home() {
 const [tasks, setTasks] = useState([])
 const [taskName, setTaskName] = useState("")

 useEffect(() => {
    axios.get('http://localhost:15555/api/tasks/')
      .then(res => {
        setTasks(res.data.data)
      })
  }, []);

 const addTask = () => {
    if (taskName !== "") {

    	axios.post('http://localhost:15555/api/tasks/', JSON.stringify({'name': taskName}))
	      .then(res => {
	      	console.log(res.data)
	      	setTasks([...tasks, res.data.data]);
	      	setTaskName("");
	      })
    }
  };

 return (
   <div className="App my-2">
        <div className="row">
            <div className="col-10 mx-auto">
             <p className="h2 todo-font">TODO LIST</p>
                <div className="row">
                	<div className="col-12 mb-4">
                		<div className="row">
	                		<div className="col-4">
	                			<input 
	                			value={taskName}
	                			onChange={(e) => setTaskName(e.target.value)} 
	                			className="form-control"/>
	                		</div>
	                		<div className="col-8">
	                			<button className="btn border" onClick={addTask}>Добавить</button>
	                		</div>
                		</div>
                	</div>

                	<div className="col-12">
                		<table className="table table-bordered">
					        <tbody>
					            <tr className="text-center">
					                <th>Задания</th>
					                <th>Просмотр на новой странице</th>
					                <th>Удаление</th>
					            </tr>
					            {tasks.length > 0 &&
					                tasks.map(task => <Task key={task.id} task={task} />)
					            }
					        </tbody>

			    		</table>
                	</div>
                </div>
                
                <Alert variant="dark">
                  <Alert.Heading> Внимание!</Alert.Heading>
                  <p>
                    Ваш <span className="todo-font">DOTO LIST</span> будет автоматически очищаться демоном каждые 2 минуты
                  </p>
                </Alert>
            </div>
        </div>
   </div>
 );
}
export default Home;