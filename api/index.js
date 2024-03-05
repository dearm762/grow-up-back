import express from 'express'

const app = express()
const PORT = 7777

app.post('/auth/sign-in', (req, res) => {
    res.send('POST request to the sign-in')
})

app.post('/auth/sign-up', (req, res) => {
    res.send('POST request to the sign-up')
})

app.post('/auth/forgot-password', (req, res) => {
    res.send('POST request to the forgot-password')
})

app.listen(PORT, () => {
    console.log(`Listening On http://185.22.67.20:${PORT}`)
})