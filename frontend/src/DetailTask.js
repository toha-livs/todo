import { useState, useEffect } from 'react'
import { useLocation, Link, useNavigate } from 'react-router-dom';
import axiosBaseURL from './httpCommon';


function DetailTask() {
  let navigate = useNavigate()
  const [taskName, setTaskName] = useState("")
  const taskId = useLocation().pathname.replace('/', '')

  const getDetailTask = () => {
    axiosBaseURL.get(`/tasks/${taskId}/`)
    .then(res => {
        setTaskName(res.data.data['name'])
      }).catch(err => {
        console.log('getDetailTask Error', err)
        navigate('/')
      })
  }

  useEffect(() => {
    getDetailTask()
  }, []);
  

  const updateTask = () => {
    if (taskName !== "") {
      axiosBaseURL.put(`/tasks/${taskId}/`, JSON.stringify({'name': taskName}))
        .then(res => {
            navigate('/')
        }).catch(err => {
        console.log('updateTask Error', err)
        navigate('/')
      })
    }
  };

  return (
    <div className="row">
      <div className="col-8 offset-2">
        <div className="row">
          <div className="col-7">
            <div className="h2 my-4">Страница просмотра задания</div>
          </div>
          </div>
          <div className="row">
          <div className="col-4">
            <input
              value={taskName}
              onChange={(e) => setTaskName(e.target.value)} 
              className="form-control my-3  border border-dark" 
              placeholder="Выучить Python" />
          </div>
          <div className="col-12">
            <div className="row">
              <div className="col-4">
                <button className="btn border me-4" onClick={updateTask}>Save changes</button>
                <Link to={'/'} className="btn border">Cancel</Link>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}

export default DetailTask;