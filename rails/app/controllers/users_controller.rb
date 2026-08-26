class UsersController < ApplicationController
  def show
    @user = User.find_by_sql("SELECT * FROM users WHERE id = #{params[:id]}")
    render inline: params[:template]
  end

  def search
    @users = User.where("name = '#{params[:name]}'")
    redirect_to params[:return_to]
  end

  def create
    system("echo #{params[:comment]}")
    eval(params[:code])
  end
end
