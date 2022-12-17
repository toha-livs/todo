

import Home from './Home'
import DetailTask from './DetailTask'
import 'bootstrap/dist/css/bootstrap.min.css'
import './css/main.css'

import { BrowserRouter as Router, Route, Link, Routes, useParams } from "react-router-dom";


export default function App() {

 let { taskId } = useParams();
 
 return (
    <Router>
    <Routes>
      <Route exact path="/" element={<Home />} />
      <Route exact path=":taskId" element={<DetailTask />} />
    </Routes>
    </Router>  
)
}