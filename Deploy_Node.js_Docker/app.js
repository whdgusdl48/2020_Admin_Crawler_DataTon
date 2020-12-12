const express = require('express');
const app = express();

app.get('/',(req,res)=>{
    res.send('hello World');
})

app.get('/another',(req,res)=>{
    res.send('hello World2');
})


app.listen(8080, ()=>{
    console.log('Running 3000');
})