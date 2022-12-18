import Axios from 'axios';

const getBaseUrl = () => {
  let url = 'http://localhost:8000'
  if (process.env.NODE_ENV == 'production') {
    url = 'https://3.75.136.149/api'
  }
  return url
}

const axiosBaseURL = Axios.create({
    baseURL: getBaseUrl()
});

export default axiosBaseURL