<?php

use Phalcon\Mvc\Model;

class Posts extends Model
{
    public $id;
    public $title;
    public $body;

	public function initialize()
    {

    }
}