<?php

class ErrorsController extends ControllerBase
{

    public function initialize(){        
        parent::initialize();
    }

	public function show404Action()
    {
        die('404');
    }

    public function show500Action()
    {
        die('500');
    }

}
