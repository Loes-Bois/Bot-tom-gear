docker-compose build
heroku container:login
heroku container:push bottom-bot --app bot-tom-gear-bot
heroku ps:stop bottom-bot --app bot-tom-gear-bot
heroku container:release bottom-bot --app bot-tom-gear-bot