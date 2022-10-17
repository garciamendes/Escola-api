import React, { useEffect } from 'react'

import { api } from './services/api'

export default function App() {
  useEffect(() => {
    api.get('http://172.25.76.66:8000/alunos')
  }, [])

  return (
    <h1>Hllo</h1>
  )
}
