$gedit setup.sh
  #Copy the code below
	      mkdir -p ~/.streamlit/
	      echo "\
              [server]\n\
              headless = true\n\
              port = $PORT\n\
              enableCORS = false\n\
              \n\
              " > ~/.streamlit/config.toml