import Axios from 'axios';

const getBaseUrl = () => {
  let url = 'localhost:8000'
  let schema = 'http'
  if (process.env.SERVER_HOST) {
    url = process.env.SERVER_HOST
  }
  if (process.env.SERVER_SECURE) {
      schema = 'https'
  }
  return schema +  '://' + url
}

const axiosBaseURL = Axios.create({
    baseURL: getBaseUrl()
});

export default axiosBaseURL